from fastapi import FastAPI, status
from app.api.routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

PREFIX = "/api/v1"

app = FastAPI(
    title="Eight",
    description="Eight is Octavio's AI assistant on his portfolio website which answers users questions about Octavio's background, projects, and experience.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix=f"{PREFIX}/chat")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health() -> dict[str, str]:
    return {"status": "healthy"}
