import os, requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
API_KEY = os.getenv("FINNHUB_KEY")

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        r = requests.get(f"https://finnhub.io/api/v1/quote?symbol=BINANCE:TRXUSDT&token={API_KEY}").json()
        harga = r.get('c', 0)
        return f"<h1 style='font-family:sans-serif;text-align:center;margin-top:50px'>TRX: ${harga}<br><small>High ${r.get('h')} | Low ${r.get('l')}</small></h1><script>setTimeout(()=>location.reload(),5000)</script>"
    except Exception as e:
        return f"<h1>Set FINNHUB_KEY dulu ko: {e}</h1>"

@app.get("/api/trx")
def api():
    r = requests.get(f"https://finnhub.io/api/v1/quote?symbol=BINANCE:TRXUSDT&token={API_KEY}").json()
    return r
