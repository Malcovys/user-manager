from fastapi import FastAPI
from app.account.routes import router as account_routes


app = FastAPI()

app.include_router(account_routes)