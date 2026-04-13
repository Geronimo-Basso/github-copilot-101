import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="SunVoyage Tours")

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def load_config():
    config_path = BASE_DIR / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    config = load_config()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "config": config,
    })


@app.get("/api/activities")
async def get_activities():
    config = load_config()
    return config.get("activities", [])


@app.get("/api/flights")
async def get_flights():
    config = load_config()
    return config.get("flights", [])


@app.get("/api/accommodations")
async def get_accommodations():
    config = load_config()
    return config.get("accommodations", [])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
