from pydantic import BaseModel, Field


class SRequestData(BaseModel):
    text_query: str
    callback_url: str = Field(example="https://example.com/callback")


class SImageBase64(BaseModel):
    result: str
