from fastapi import FastAPI

app = FastAPI(title="AWS Security Gate API")


@app.get("/")
def home():
    return {
        "message": "AWS Security Gate Application is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }