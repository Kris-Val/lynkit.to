"use client";

import axios from "axios";
import React, {useState} from "react";
import {Lock, Mail} from "lucide-react";
import {Button} from "@/components/ui/button";
import {Card, CardContent, CardHeader, CardTitle} from "@/components/ui/card";
import {Separator} from "@/components/ui/separator";
import {auth} from "@/api/auth";
import {CredentialResponse, GoogleLogin, GoogleOAuthProvider,} from "@react-oauth/google";

export default function Login() {
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        setError(null);
        setIsLoading(true);

        try {
            console.log("Login attempt:", {username, password});
            if (!username || !password) {
                throw new Error("Username and password are required");
            }

            const response = await auth.login({username, password});
            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail ?? "Login failed");
            }

            console.log("Login successful");
        } catch (err: unknown) {
            setError(
                err instanceof Error
                    ? err.message
                    : "Login failed. Please try again."
            );
        } finally {
            setIsLoading(false);
        }
    }

    const handleGoogleSuccess = async (res: CredentialResponse) => {
        setError(null);
        setIsLoading(true);
        console.log("Google response:", res);

        try {
            // 1) Try to log in via token exchange
            await axios.post(
                "http://localhost:8000/_allauth/app/v1/auth/provider/token",
                {
                    provider: "google",
                    process: "login",
                    token: {
                        id_token: res.credential,
                        client_id: process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID, // ← your Google client ID
                    },
                },
                {withCredentials: true}
            );
            console.log("Google login successful");
            // …your post-login logic here (redirect, fetch user, etc.)…
        } catch (err: any) {
            // 2) If 401, we need to create (signup) the user
            const status = err.response?.status;
            const sessionToken = err.response?.data?.meta?.session_token;
            if (status === 401 && sessionToken) {
                try {
                    await axios.get(
                        "http://localhost:8000/_allauth/app/v1/auth/provider/signup",
                        {
                            headers: {"X-Session-Token": sessionToken},
                            withCredentials: true,
                        }
                    );
                    console.log("Google signup + login successful");
                    // …post-signup logic here…
                } catch (signupErr: unknown) {
                    setError(
                        signupErr instanceof Error
                            ? signupErr.message
                            : "Google signup failed. Please try again."
                    );
                }
            } else {
                setError(
                    err instanceof Error
                        ? err.message
                        : "Google login failed. Please try again."
                );
            }
        } finally {
            setIsLoading(false);
        }
    };

    const handleGoogleError = () => {
        setError("Google login failed. Please try again.");
    };

    return (
        <GoogleOAuthProvider
            clientId={process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID!}
        >
            <Card className="max-w-md mx-auto mt-12 shadow-lg">
                <CardHeader>
                    <CardTitle className="text-2xl text-center">Sign In</CardTitle>
                </CardHeader>
                <CardContent>
                    {error && <p className="text-red-600 mb-4 text-center">{error}</p>}

                    <form onSubmit={handleSubmit} className="space-y-4">
                        <label className="block">
                            <div className="flex items-center mb-1 text-sm font-medium">
                                <Mail className="w-4 h-4 mr-1 text-gray-500"/> Username
                            </div>
                            <input
                                type="text"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                                placeholder="Enter your username"
                            />
                        </label>

                        <label className="block">
                            <div className="flex items-center mb-1 text-sm font-medium">
                                <Lock className="w-4 h-4 mr-1 text-gray-500"/> Password
                            </div>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                                className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                                placeholder="Enter your password"
                            />
                        </label>

                        <Button
                            type="submit"
                            disabled={isLoading}
                            className="w-full py-2 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white rounded-lg"
                        >
                            {isLoading ? "Signing in..." : "Sign In"}
                        </Button>
                    </form>

                    <div className="my-4">
                        <Separator/>
                        <div className="text-center text-sm text-gray-500 -mt-3 bg-white px-2">
                            or
                        </div>
                    </div>

                    <div className="flex justify-center">
                        <GoogleLogin
                            onSuccess={handleGoogleSuccess}
                            onError={handleGoogleError}
                        />
                    </div>

                    <div className="mt-4 text-center text-sm text-gray-600">
                        Don't have an account?{" "}
                        <a href="/signup" className="text-purple-600 hover:underline">
                            Sign up
                        </a>
                    </div>
                </CardContent>
            </Card>
        </GoogleOAuthProvider>
    );
}
