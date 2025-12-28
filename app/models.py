from pydantic import BaseModel, Field

MIN_VALUE = -1_000_000
MAX_VALUE = 1_000_000


class AddRequest(BaseModel):
    a: int = Field(..., ge=MIN_VALUE, le=MAX_VALUE)
    b: int = Field(..., ge=MIN_VALUE, le=MAX_VALUE)


class AddResponse(BaseModel):
    result: int
