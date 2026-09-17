from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.database import get_db

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict:
    """Basic liveness check — no DB touch."""
    return {"status": "ok", "app": settings.app_name, "env": settings.app_env}


@app.get("/health/db")
def health_check_db(db: Session = Depends(get_db)) -> dict:
    """Confirms the backend can actually reach Postgres."""
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
