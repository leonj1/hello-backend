# hello-backend

Minimal FastAPI app with a hello-world weather endpoint.

Run locally:

- Create a virtualenv and install deps: `pip install -r requirements.txt`
- Start server: `uvicorn app.main:app --reload`
- Open `http://127.0.0.1:8000/weather` to see `{ "message": "Hello, world" }`

Endpoints:

- `GET /health` – health check `{ "status": "ok" }`
- `GET /` – Swagger UI
- `GET /weather` – hello world for weather
