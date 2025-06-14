"use client";

import {useEffect, useState} from "react";
import Link from "next/link";
import {ChevronDown, LogOut, Mail, Settings, ShieldCheck, User, Users} from "lucide-react";

export default function Header() {
    const [user, setUser] = useState<{ username?: string; email?: string } | null>(null);
    const [dropdownOpen, setDropdownOpen] = useState(false);

    useEffect(() => {
        fetch("/api/v1/auth/status", {
            credentials: "include", // include cookies for session authentication
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.authenticated) {
                    setUser({username: data.username, email: data.email});
                } else {
                    setUser(null);
                }
            })
            .catch(() => setUser(null));
    }, []);

    return (
        <header className="bg-white shadow-sm border-b">
            <div className="container mx-auto px-4 py-4 flex items-center justify-between">
                {/* Logo */}
                <Link href="/" className="flex items-center space-x-2">
                    <div
                        className="w-8 h-8 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
                        <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={2}
                                d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
                            />
                        </svg>
                    </div>
                    <span
                        className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
            LinkHub
          </span>
                </Link>

                {/* Right side: navigation */}
                <div className="flex items-center space-x-4">
                    {user ? (
                        <div className="relative">
                            <button
                                onClick={() => setDropdownOpen(!dropdownOpen)}
                                className="flex items-center space-x-2 text-gray-700 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
                            >
                                <User className="w-5 h-5"/>
                                <span>{user.username || user.email}</span>
                                <ChevronDown className="w-4 h-4"/>
                            </button>
                            {dropdownOpen && (
                                <div className="absolute right-0 mt-2 w-52 bg-white rounded-md shadow-lg z-50 border">
                                    <ul className="py-1 text-sm text-gray-700">
                                        <li>
                                            <Link href="/accounts/"
                                                  className="flex items-center gap-2 px-4 py-2 hover:bg-gray-100">
                                                <Settings className="w-4 h-4"/>
                                                Profile
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href="/accounts/email/"
                                                  className="flex items-center gap-2 px-4 py-2 hover:bg-gray-100">
                                                <Mail className="w-4 h-4"/>
                                                Change Email
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href="/accounts/password/change/"
                                                  className="flex items-center gap-2 px-4 py-2 hover:bg-gray-100">
                                                <ShieldCheck className="w-4 h-4"/>
                                                Change Password
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href="/accounts/social/connections/"
                                                  className="flex items-center gap-2 px-4 py-2 hover:bg-gray-100">
                                                <Users className="w-4 h-4"/>
                                                Social Accounts
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href="/accounts/logout/"
                                                  className="flex items-center gap-2 px-4 py-2 text-red-600 hover:bg-red-50">
                                                <LogOut className="w-4 h-4"/>
                                                Sign Out
                                            </Link>
                                        </li>
                                    </ul>
                                </div>
                            )}
                        </div>
                    ) : (
                        <>
                            <Link href="/accounts/login/"
                                  className="text-gray-600 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium">
                                Sign In
                            </Link>
                            <Link
                                href="/accounts/signup/"
                                className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium transition-all duration-200"
                            >
                                Sign Up
                            </Link>
                        </>
                    )}
                </div>
            </div>
        </header>
    );
}
