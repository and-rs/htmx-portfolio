import subprocess


if __name__ == "__main__":
    _ = subprocess.run(
        [
            "tailwindcss",
            "-i",
            "static/styles/globals.css",
            "-o",
            "static/output.css",
            "--minify",
            "--watch",
        ]
    )
