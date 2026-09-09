from fastapi import FastAPI
from app.routes.routes import router


app = FastAPI(title="PawMart API")
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to PawMart API"}