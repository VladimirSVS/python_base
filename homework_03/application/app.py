from fastapi import FastAPI
from schemas import PingOut


app = FastAPI()

@app.get("/ping/",response_model=PingOut)
def ping() -> PingOut:
    return PingOut()
