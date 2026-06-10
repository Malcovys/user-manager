from fastapi import FastAPI

from account.middlewares import auth_middleware, log_middleware


app = FastAPI()

app.middleware("http")(auth_middleware)
app.middleware("http")(log_middleware)
