from fastapi import FastAPI, HTTPException
from app.config import settings
from app.brokers.exnova.client import ExnovaClient

app = FastAPI(title="Exnova FastAPI DEMO", version="1.0.0")
client = ExnovaClient(settings.EXNOVA_EMAIL, settings.EXNOVA_PASSWORD, settings.EXNOVA_MODE)

@app.get("/")
def root():
    return {"app": "Exnova FastAPI DEMO", "mode": settings.EXNOVA_MODE, "trading_enabled": False}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/broker/status")
def broker_status():
    return client.status()

@app.post("/broker/connect")
def broker_connect():
    try:
        return client.connect()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

@app.post("/broker/disconnect")
def broker_disconnect():
    return client.disconnect()

@app.get("/broker/account")
def broker_account():
    if not client.connected:
        raise HTTPException(status_code=409, detail="Broker is not connected")
    return client.account()
