import json
from pathlib import Path
from app.dependencies import templates


def setup_img_loader(image_path: Path):
    if image_path.exists():
        with open(image_path) as f:
            raw_images = json.load(f)
            image_metadata = {img["slug"]: img for img in raw_images}
    else:
        image_metadata = {}

    # fmt: off
    templates.env.globals["IMAGES"] = image_metadata  # pyright: ignore[reportUnknownMemberType]
