from fastapi import FastAPI, Body,HTTPException
from starlette.middleware.cors import CORSMiddleware
from domain.check import check_router
from pydantic import BaseModel
from domain.check import check_crud

app = FastAPI()

class ContentCheckResult(BaseModel):
    result: str



@app.post("/letter/write", response_model=ContentCheckResult)
async def check_content(content: str = Body("default_content", embed=True)):
    try:
        # 여기에 AI 모델로 content를 확인하는 로직 추가
        dd = check_crud.sentence_predict(content)
        # 예시: 간단히 "1"으로 응답 (정상 콘텐츠로 판단)
        return {"result": dd}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))