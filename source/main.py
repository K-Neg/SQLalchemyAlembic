import uvicorn
from fastapi import FastAPI
from database import retrieve_all_users
import logging

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logging.info(msg="Api started")


@app.get("/")
def root():
    return {"message": "I am online"}


@app.get("/users")
async def get_users():
    users = await retrieve_all_users()
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
