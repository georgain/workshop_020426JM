from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import multiply, resta, sum


app = FastAPI(title="Calculator API")


class OperationInput(BaseModel):
    a: int
    b: int


class OperationResult(BaseModel):
    result: int


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Calculator API is running"}


@app.post("/suma", response_model=OperationResult)
def suma(payload: OperationInput) -> OperationResult:
    return OperationResult(result=sum(payload.a, payload.b))


@app.post("/resta", response_model=OperationResult)
def subtract(payload: OperationInput) -> OperationResult:
    return OperationResult(result=resta(payload.a, payload.b))


@app.post("/multiplicacion", response_model=OperationResult)
def multiplicacion(payload: OperationInput) -> OperationResult:
    return OperationResult(result=multiply(payload.a, payload.b))
