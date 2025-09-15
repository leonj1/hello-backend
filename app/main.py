from fastapi import FastAPI

app = FastAPI(title="Hello Weather API")


@app.get("/", summary="Health check")
def read_root():
    return {"status": "ok"}


@app.get("/weather", summary="Hello world weather endpoint")
def read_weather():
    return {"message": "Hello, world"}

