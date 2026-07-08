"""Minimal, interview-friendly FastAPI app."""

from fastapi import FastAPI
from pydantic import BaseModel


class HomeResponse(BaseModel):
    """Structured response contract for the home endpoint."""

    message: str
    purpose: str


app = FastAPI(
    title="Interview Ready FastAPI",
    description="A clean starter API that demonstrates good FastAPI basics.",
    version="1.0.0",
)


@app.get("/", response_model=HomeResponse, tags=["General"])
def home() -> HomeResponse:
    """Return a welcome message and app purpose."""

    return HomeResponse(
        message="Hello, World!",
        purpose="Template for clean and readable FastAPI interview projects",
    )