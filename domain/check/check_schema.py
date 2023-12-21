from pydantic import BaseModel, validator


class Check(BaseModel):
    content: str
    true_check: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('편지 내용이 비어 있습니다')
        return v


