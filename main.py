from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}


@app.get("/webhook")
def verify_webhook(
    hub_mode: str = None,
    hub_challenge: str = None,
    hub_verify_token: str = None
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return PlainTextResponse(hub_challenge)

    return PlainTextResponse("Verification failed", status_code=403)
