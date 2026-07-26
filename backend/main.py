import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.generate import router as generate_router
from dotenv import load_dotenv

# Load .env from the backend directory
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

app = FastAPI(title="AI Project Idea Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(generate_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("SERVER_PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)
