from fastapi import FastAPI

from app.api.routes import products, users, login
from app.core.logging import setup_logging
from app.core.middleware import setup_middleware


app = FastAPI()

setup_logging()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(login.router)

setup_middleware(app)