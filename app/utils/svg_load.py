from pathlib import Path
from fastapi.templating import Jinja2Templates


def setup_svg_loader(templates: Jinja2Templates):
    def load_svg_content(icon_name: str) -> str:
        svg_path = Path("static/icons") / f"{icon_name}.svg"
        try:
            return svg_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="size-5"><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="12">?</text></svg>'

    # fmt:off
    templates.env.globals["load_svg_content"] = (load_svg_content)  # pyright: ignore[reportUnknownMemberType]
