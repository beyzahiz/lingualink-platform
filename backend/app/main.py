from fastapi import FastAPI
from app.routers import user_auth

app = FastAPI(title="LinguaLink API", version="1.0.0")

# Router'ı ana uygulamaya dahil ediyorum
app.include_router(user_auth.router)

@app.get("/")
def read_root():
    return {"message": "LinguaLink backend çalışıyor"}
