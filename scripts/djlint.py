import subprocess
from pathlib import Path

if __name__ == "__main__":
    _ = subprocess.run(
        [
            "djlint",
            "--reformat",
            "--profile=jinja",
            "--extension=jinja",
            *Path("templates").glob("**/*.jinja"),
        ]
    )
