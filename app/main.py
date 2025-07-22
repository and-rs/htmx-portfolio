import arel
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import DEBUG

app = FastAPI(title="AI Categorizer")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

if DEBUG:
    hot_reload = arel.HotReload(paths=[arel.Path("app/templates")])

    async def hot_reload_wrapper(websocket: WebSocket):
        await hot_reload(websocket.scope, websocket.receive, websocket.send)

    app.add_websocket_route(
        "/hot-reload", route=hot_reload_wrapper, name="hot-reload"
    )

    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = True
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    return templates.TemplateResponse("home/home.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about_section(request: Request):
    return templates.TemplateResponse("about/about.html", {"request": request})


@app.get("/json", response_class=JSONResponse)
async def json_example():
    return {"Hello": "World"}
