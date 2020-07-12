"""Fast API Entry Point"""

# Imports from Stdlib
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

# Imports from sql_app within the project
from sql_app import models
from sql_app.database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


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
    Creates stocks and stores it in the sql_app
    :return: JSON response post creation
    :rtype: dict
    """
    return {
        "code": "success",
        "message": "stock created"
    }
