import subprocess


if __name__ == "__main__":
    _ = subprocess.run(
        [
            "tailwindcss",
            "-i",
            "static/input.css",
            "-o",
            "static/output.css",
            "--watch",
        ]
    )
