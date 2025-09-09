from pathlib import Path
from PIL import Image
import json
import hashlib

INPUT_DIR = Path("raw-images")
OUTPUT_DIR = Path("static") / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SIZES = [320, 640, 960, 1280, 1920]
QUALITIES = {
    "avif": 55,
    "webp": 75,
    "jpg": 78,
}


def hash_bytes(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()[:8]


def strip_exif(img: Image.Image) -> Image.Image:
    return img.copy()


def process_image(path: Path):
    with open(path, "rb") as f:
        data = f.read()
    file_hash = hash_bytes(data)

    slug = f"{path.stem}-{file_hash}"
    img = Image.open(path)
    w, h = img.size
    ratio = h / w if w > 0 else 1

    img = strip_exif(img)

    # Generate variants
    for width in SIZES:
        height = int(width * ratio)
        resized = img.resize((width, height), Image.Resampling.LANCZOS)

        avif_path = OUTPUT_DIR / f"{slug}-{width}.avif"
        resized.save(
            avif_path, format="AVIF", quality=QUALITIES["avif"], speed=6
        )

        webp_path = OUTPUT_DIR / f"{slug}-{width}.webp"
        resized.save(
            webp_path, format="WEBP", quality=QUALITIES["webp"], method=6
        )

        jpg_path = OUTPUT_DIR / f"{slug}-{width}.jpg"
        resized.convert("RGB").save(
            jpg_path,
            format="JPEG",
            quality=QUALITIES["jpg"],
            optimize=True,
            progressive=True,
        )

    thumb = img.copy()
    thumb.thumbnail((24, 24), Image.Resampling.LANCZOS)
    thumb_path = OUTPUT_DIR / f"{slug}-blur.jpg"
    thumb.convert("RGB").save(thumb_path, format="JPEG", quality=20)

    metadata = {
        "slug": slug,
        "width": w,
        "height": h,
        "aspect_ratio": ratio,
        "sizes": SIZES,
        "formats": ["avif", "webp", "jpg"],
        "placeholder": f"{slug}-blur.jpg",
    }
    with open(OUTPUT_DIR / f"{slug}.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"✔ Processed: {path.name} → {slug}")


if __name__ == "__main__":
    for file in INPUT_DIR.iterdir():
        if file.is_file() and file.suffix.lower() in (".jpg", ".jpeg", ".png"):
            process_image(file)
