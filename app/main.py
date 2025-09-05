# pyright: reportUnknownMemberType=false
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

from app.api import router
from app.config import DEBUG
from app.dependencies import templates
from app.utils.svg_load import setup_svg_loader

app = FastAPI(title="Juan Bautista Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
setup_svg_loader(templates)

if DEBUG:
    import arel

    hot_reload = arel.HotReload(
        paths=[arel.Path("templates"), arel.Path("static/styles")]
    )

    async def hot_reload_wrapper(websocket: WebSocket):
        await hot_reload(websocket.scope, websocket.receive, websocket.send)

    app.add_websocket_route(
        "/hot-reload", route=hot_reload_wrapper, name="hot-reload"
    )

    # annoying warnings related to unknow types from libraries
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["hot_reload"] = hot_reload
    templates.env.globals["DEBUG"] = True
