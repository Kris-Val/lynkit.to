import {Link} from "lucide-react";
import {Button} from "@/components/ui/button";

const Header = () => {
    return (
        <header className="container mx-auto px-4 py-6 flex items-center justify-between">
            <a href="/" className="flex items-center space-x-2">
                <div
                    className="w-8 h-8 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
                    <Link className="w-5 h-5 text-white"/>
                </div>
                <span
                    className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
          LinkHub
        </span>
            </a>
            <div className="flex items-center space-x-4">
                <Button variant="ghost" className="text-gray-600 hover:text-gray-900" asChild>
                    <a href="/login">Log in</a>
                </Button>
                <Button
                    className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white">
                    <a href="/signup">Sign up</a>
                </Button>
            </div>
        </header>
    );
};

export default Header;