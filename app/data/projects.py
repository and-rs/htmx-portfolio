def get_projects():
    return [
        {
            "id": "connect-bun",
            "title": "Connect-bun",
            "subtitle": "High-performance Connect RPC adapter for Bun",
            "tech": ["Bun", "Connect RPC", "TypeScript", "Web Streams"],
            "bullets": [
                "Built a high-performance adapter for Connect RPC on Bun, hitting 140k req/s (2.1x faster than Node.js) by mapping the `UniversalHandler` directly to Bun’s native `fetch`",
                "Implemented a streaming pipeline for large uploads (>100MB) that keeps memory usage flat (O(1)), using standard Web Streams to avoid loading files into RAM",
                "Created a benchmark suite to measure latency and garbage collection, validating exactly where Bun’s I/O primitives outperform the traditional Node.js event loop",
            ],
            "links": {"repo": "https://github.com/and-rs/connect-bun", "demo": None},
            "media": [],
            "order": 2,
        },
    ]
