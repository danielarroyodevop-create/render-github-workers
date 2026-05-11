from fastapi import FastAPI
import httpx

app = FastAPI()

WORKERS = [
    "https://worker1.onrender.com",
    "https://worker2.onrender.com"
]

@app.get("/run")
async def run():
    results = []

    async with httpx.AsyncClient(timeout=30) as client:
        for w in WORKERS:
            try:
                r = await client.get(f"{w}/compute")
                results.append({"worker": w, "result": r.json()})
            except Exception as e:
                results.append({"worker": w, "error": str(e)})

    return {"status": "ok", "results": results}
