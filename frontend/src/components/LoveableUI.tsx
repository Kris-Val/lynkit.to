import {ArrowRight, Check, Link, Users, BarChart3, Palette} from "lucide-react";
import {Button} from "@/components/ui/button";
import {Card, CardContent} from "@/components/ui/card";

const Index = () => {
    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-blue-50">
            {/* Hero Section */}
            <section className="container mx-auto px-4 py-20 text-center">
                <div className="max-w-4xl mx-auto">
                    <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-purple-600 via-blue-600 to-indigo-600 bg-clip-text text-transparent leading-tight">
                        One link to rule them all
                    </h1>
                    <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
                        Connect your audience to all of your content with one simple link in bio.
                        Share everything you create, curate and sell from your Instagram, TikTok, Twitter and other
                        social media profiles.
                    </p>
                    <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
                        <Button size="lg"
                                className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white px-8 py-4 text-lg group">
                            Get started for free
                            <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform"/>
                        </Button>
                        <Button size="lg" variant="outline"
                                className="px-8 py-4 text-lg border-gray-300 hover:border-gray-400">
                            See how it works
                        </Button>
                    </div>

                    {/* Demo Preview */}
                    <div className="relative max-w-sm mx-auto">
                        <div className="bg-white rounded-3xl shadow-2xl p-6 border">
                            <div className="flex items-center justify-center mb-4">
                                <div
                                    className="w-16 h-16 bg-gradient-to-r from-purple-400 to-blue-400 rounded-full flex items-center justify-center">
                                    <span className="text-white font-bold text-xl">JD</span>
                                </div>
                            </div>
                            <h3 className="font-semibold text-gray-900 mb-2">@johndoe</h3>
                            <p className="text-sm text-gray-600 mb-4">Digital creator & entrepreneur</p>
                            <div className="space-y-3">
                                {[
                                    "My Latest Blog Post",
                                    "YouTube Channel",
                                    "Shop My Products",
                                    "Book a Call"
                                ].map((link, index) => (
                                    <div key={index}
                                         className="bg-gray-50 hover:bg-gray-100 rounded-lg p-3 text-sm font-medium text-gray-800 transition-colors cursor-pointer">
                                        {link}
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="py-20 bg-white">
                <div className="container mx-auto px-4">
                    <div className="text-center mb-16">
                        <h2 className="text-4xl font-bold mb-4 text-gray-900">
                            Everything you need to share your story
                        </h2>
                        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
                            Powerful features to help you connect with your audience and grow your brand.
                        </p>
                    </div>

                    <div className="grid md:grid-cols-3 gap-8">
                        {[
                            {
                                icon: Link,
                                title: "Unlimited Links",
                                description: "Add as many links as you want. No limits, no restrictions."
                            },
                            {
                                icon: Palette,
                                title: "Custom Themes",
                                description: "Personalize your page with beautiful themes and custom colors."
                            },
                            {
                                icon: BarChart3,
                                title: "Analytics",
                                description: "Track clicks and see which content resonates with your audience."
                            },
                            {
                                icon: Users,
                                title: "Social Integration",
                                description: "Connect all your social media profiles in one place."
                            },
                            {
                                icon: Check,
                                title: "Mobile Optimized",
                                description: "Your page looks perfect on every device, every time."
                            },
                            {
                                icon: ArrowRight,
                                title: "Easy Setup",
                                description: "Get started in minutes. No technical skills required."
                            }
                        ].map((feature, index) => (
                            <Card key={index}
                                  className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300">
                                <CardContent className="p-6 text-center">
                                    <div
                                        className="w-12 h-12 bg-gradient-to-r from-purple-100 to-blue-100 rounded-lg flex items-center justify-center mx-auto mb-4">
                                        <feature.icon className="w-6 h-6 text-purple-600"/>
                                    </div>
                                    <h3 className="text-xl font-semibold mb-2 text-gray-900">{feature.title}</h3>
                                    <p className="text-gray-600">{feature.description}</p>
                                </CardContent>
                            </Card>
                        ))}
                    </div>
                </div>
            </section>

            {/* Social Proof */}
            <section className="py-20 bg-gradient-to-r from-purple-600 to-blue-600 text-white">
                <div className="container mx-auto px-4 text-center">
                    <h2 className="text-4xl font-bold mb-8">
                        Trusted by creators worldwide
                    </h2>
                    <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
                        <div>
                            <div className="text-4xl font-bold mb-2">1M+</div>
                            <div className="text-purple-100">Active users</div>
                        </div>
                        <div>
                            <div className="text-4xl font-bold mb-2">10M+</div>
                            <div className="text-purple-100">Links clicked</div>
                        </div>
                        <div>
                            <div className="text-4xl font-bold mb-2">99.9%</div>
                            <div className="text-purple-100">Uptime</div>
                        </div>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="py-20 bg-gray-50">
                <div className="container mx-auto px-4 text-center">
                    <h2 className="text-4xl font-bold mb-4 text-gray-900">
                        Ready to get started?
                    </h2>
                    <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
                        Join millions of creators who use LinkHub to share their content and grow their audience.
                    </p>
                    <Button size="lg"
                            className="bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white px-8 py-4 text-lg group">
                        Create your LinkHub for free
                        <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform"/>
                    </Button>
                </div>
            </section>

            {/* Footer */}
            <footer className="bg-gray-900 text-white py-12">
                <div className="container mx-auto px-4">
                    <div className="grid md:grid-cols-4 gap-8">
                        <div>
                            <div className="flex items-center space-x-2 mb-4">
                                <div
                                    className="w-8 h-8 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
                                    <Link className="w-5 h-5 text-white"/>
                                </div>
                                <span className="text-xl font-bold">LinkHub</span>
                            </div>
                            <p className="text-gray-400">
                                The simple way to share everything you create, curate and sell online.
                            </p>
                        </div>
                        <div>
                            <h4 className="font-semibold mb-4">Product</h4>
                            <ul className="space-y-2 text-gray-400">
                                <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Pricing</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Templates</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-semibold mb-4">Support</h4>
                            <ul className="space-y-2 text-gray-400">
                                <li><a href="#" className="hover:text-white transition-colors">Help Center</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Status</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-semibold mb-4">Company</h4>
                            <ul className="space-y-2 text-gray-400">
                                <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                                <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
                            </ul>
                        </div>
                    </div>
                    <div className="border-t border-gray-800 mt-12 pt-8 text-center text-gray-400">
                        <p>&copy; 2024 LinkHub. All rights reserved.</p>
                    </div>
                </div>
            </footer>
        </div>
    );
};

export default Index;
