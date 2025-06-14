import type {NextConfig} from "next";

const nextConfig: NextConfig = {
    output: 'export',
    // assetPrefix: '/static'
    allowedDevOrigins: ["http://127.0.0.1:8000", "127.0.0.1"],
    trailingSlash: true,
};

export default nextConfig;
