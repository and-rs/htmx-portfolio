import subprocess
from pathlib import Path

if __name__ == "__main__":
    cmd = [
        "djlint",
        "--reformat",
        "--profile=jinja",
        "--extension=jinja",
        *Path("templates").glob("**/*.jinja"),
    ]
    _ = subprocess.run(cmd)
