"use client";

import React, {useEffect, useState} from "react";
import {Mail, Lock} from "lucide-react";
import {Button} from "@/components/ui/button";
import {Card, CardContent, CardHeader, CardTitle} from "@/components/ui/card";
import {auth} from "@/api/auth";

export default function SignUpForm() {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [username, setUsername] = useState<string>("");
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<boolean>(false);

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        setError(null);

        try {
            // Pass CSRF token into signUp API call
            const res = await auth.signUp({email, username, password});
            if (!res.ok) {
                const data = await res.json();
                new Error(data.detail ?? "Signup failed");
            }
            setSuccess(true);
        } catch (err: unknown) {
            if (err instanceof Error) {
                setError(err.message);
            } else {
                setError(String(err));
            }
        }
    }

    if (success) {
        return (
            <Card className="max-w-sm mx-auto mt-12">
                <CardContent className="text-center">
                    <h2 className="text-2xl font-semibold mb-4">🎉 Welcome aboard!</h2>
                    <p className="text-gray-600">
                        Signup successful. Please check your email to confirm your account.
                    </p>
                </CardContent>
            </Card>
        );
    }

    return (
        <Card className="max-w-sm mx-auto mt-12 shadow-lg">
            <CardHeader>
                <CardTitle className="text-2xl text-center">Sign Up</CardTitle>
            </CardHeader>
            <CardContent>
                {error && <p className="text-red-600 mb-4 text-center">{error}</p>}
                <form onSubmit={handleSubmit} className="space-y-4">
                    <label className="block">
                        <div className="flex items-center mb-1 text-sm font-medium">
                            <Mail className="w-4 h-4 mr-1 text-gray-500"/> Email
                        </div>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                            className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                        />
                    </label>
                    <label className="block">
                        <div className="flex items-center mb-1 text-sm font-medium">
                            <Mail className="w-4 h-4 mr-1 text-gray-500"/> Username
                        </div>
                        <input
                            type="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                            className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
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
                        />
                    </label>

                    <Button
                        type="submit"
                        className="w-full py-2 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white rounded-lg"
                    >
                        Create account
                    </Button>
                </form>
            </CardContent>
        </Card>
    );
}
