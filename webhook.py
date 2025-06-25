import json
import logging
from fastapi import FastAPI, Request

from config import config

app = FastAPI()


@app.post("/yookassa")
async def yookassa_webhook(request: Request):
    payload = await request.json()
    payment_id = payload.get("object", {}).get("id")
    if payment_id:
        logging.info("Received payment webhook: %s", payment_id)
        try:
            with open("payments.json", "r", encoding="utf-8") as f:
                payments = json.load(f)
        except Exception:
            payments = {}
        payments[payment_id] = payload
        with open("payments.json", "w", encoding="utf-8") as f:
            json.dump(payments, f, ensure_ascii=False, indent=2)
    return {"status": "ok"}
