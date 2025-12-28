from fastapi import FastAPI

from .models import AddRequest, AddResponse

app = FastAPI(title="FastAPI Practice CI", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/add", response_model=AddResponse)
def add(req: AddRequest) -> AddResponse:
    return AddResponse(result=req.a + req.b)
