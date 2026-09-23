from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FINNHUB_KEY = os.getenv("FINNHUB_KEY", "")
SYMBOL = "BINANCE:TRXUSDT"

@app.get("/")
def root():
    price = high = low = 0
    try:
        if FINNHUB_KEY:
            url = f"https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token={FINNHUB_KEY}"
            r = requests.get(url, timeout=5).json()
            price = r.get("c", 0)
            high = r.get("h", 0)
            low = r.get("l", 0)
    except:
        pass
    
    if price == 0:
        price = 0.3429
        high = 0.3472
        low = 0.3403

    return {
        "symbol": "TRX/USDT",
        "price": price,
        "high": high,
        "low": low,
        "time": datetime.now().isoformat(),
        "text": f"TRX: ${price} High ${high} | Low ${low}",
        "status": "Active - LIKX Official"
    }

@app.get("/tv")
def tv():
    data = root()
    return f"{data['price']},{data['high']},{data['low']}"
