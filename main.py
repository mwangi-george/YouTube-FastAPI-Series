from fastapi import FastAPI
from app.routes.test import create_test_router


def create_app() -> FastAPI:

    app = FastAPI()
    test_router = create_test_router()
    app.include_router(test_router)
    return app


app = create_app()
