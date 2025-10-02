import subprocess
import shutil
import platform


def get_tailwind_command():
    if platform.system() == "Linux" and shutil.which("nixos-version"):
        return "/run/current-system/sw/bin/tailwindcss"
    else:
        return "tailwindcss"


if __name__ == "__main__":
    tailwind_bin = get_tailwind_command()

    _ = subprocess.run(
        [
            tailwind_bin,
            "-i",
            "static/styles/globals.css",
            "-o",
            "static/output.css",
            "--watch",
            "--minify",
        ]
    )
