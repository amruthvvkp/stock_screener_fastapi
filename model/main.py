"""Fast API Entry Point"""

from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    Dashboard/Home page
    :return: JSON response for homepage
    :rtype: dict
    """
    return templates.TemplateResponse("home.html", {
        "request": request,
        "somevar": 2
    })


@app.post("/stock")
def create_stock():
    """
    Creates stocks and stores it in the database
    :return: JSON response post creation
    :rtype: dict
    """
    return {
        "code": "success",
        "message": "stock created"
    }
