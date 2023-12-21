from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from database import get_db
from domain.check import check_crud


router = APIRouter(
    prefix="/api",
)


@router.get('/letter/write')
def check_letter(db: Session = Depends(get_db)):
    letter_contents = check_crud.get_response_letter()
    result = check_crud.sentence_predict(letter_contents)

    json_object = json.dumps(result)

    return json_object
