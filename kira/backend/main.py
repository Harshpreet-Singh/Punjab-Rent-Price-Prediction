from fastapi import FastAPI

app = FastAPI(
    title="KIRA API",
    description="Punjab Rent Intelligence API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "KIRA API is running",
        "status": "ok",
    }