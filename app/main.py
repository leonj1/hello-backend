from fastapi import FastAPI

# Serve Swagger UI at the root path
app = FastAPI(title="Hello Weather API", docs_url="/", redoc_url=None)


@app.get("/health", summary="Health check")
def read_root():
    return {"status": "ok"}


@app.get("/weather", summary="Hello world weather endpoint")
def read_weather():
    return {"message": "Hello, world"}
