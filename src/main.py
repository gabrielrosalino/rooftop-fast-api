import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import rankings

app = FastAPI()

app.include_router(rankings.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
