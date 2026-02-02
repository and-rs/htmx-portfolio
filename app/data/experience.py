def get_experiences():
    return [
        {
            "title": "Data Engineer, Reliability",
            "company": "LogicSource",
            "start_date": "2025-05",
            "end_date": None,
            "location": "Remote, US",
            "bullets": [
                "Replaced manual, error-prone Excel quality checks with a Python test suite, processing 100k+ monthly records across 40+ business cases using Polars.",
                "Built an API orchestration layer to replace brittle UI-based data flows, ensuring all execution is version-controlled and reproducible in production.",
                "Refactored massive monolithic Jupyter notebooks into modular Python projects, adding validation gates that cut pipeline processing time in half.",
                "Standardized messy, manual data runs into deterministic pipelines with strict contracts, shifting the workflow from 'fire-fighting' to a stable system architecture.",
            ],
        },
        {
            "title": "Platform Engineer",
            "company": "Iridium",
            "start_date": "2023-12",
            "end_date": None,
            "location": "Remote, Global",
            "bullets": [
                "Benchmarked Connect RPC streaming, finding a 2.1x speed advantage in Bun over Node.js and fixing backpressure issues for 100MB+ file uploads.",
                "Building a custom HTTP/1.1 server in Zig to master manual memory management and low-level optimization in resource-constrained environments.",
                "Created a Neovim/Lua developer environment that earned 75+ stars on GitHub; contributed core concurrency fixes to the Yazi file manager.",
                "Designed a verifiable file system using a simplified blockchain ledger (SHA-256 hash chaining) in Postgres to guarantee data immutability.",
            ],
        },
    ]
