import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Diabetes Awareness")

BASE_DIR = Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def load_content() -> dict:
    with open(BASE_DIR / "data" / "content.json", encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
def index(request: Request):
    data = load_content()
    return templates.TemplateResponse(request, "index.html", data)
