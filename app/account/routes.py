from fastapi import APIRouter, Depends
from app.dependencies import db_session

router = APIRouter()

@router.get('/auth')
async def auth(db = Depends(db_session)):
    return 'Hello'