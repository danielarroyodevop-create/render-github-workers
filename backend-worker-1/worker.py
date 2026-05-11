from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/compute")
def compute():
    time.sleep(1)
    result = random.randint(1, 1000000)
    return {"value": result}
