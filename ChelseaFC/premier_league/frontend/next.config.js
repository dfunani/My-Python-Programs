/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['upload.wikimedia.org', "cdn.sportdataapi.com"],
  },
}

module.exports = nextConfig
