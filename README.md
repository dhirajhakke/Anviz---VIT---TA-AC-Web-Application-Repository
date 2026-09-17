# Xthings Anviz Attendance / Access / IoT Platform

Base project scaffold. **No API endpoints or DB schema yet** — this is just the
skeleton: frontend, backend, and dockerised Postgres wired together and talking
to each other.

## Stack

- **Frontend**: React + Vite
- **Backend**: FastAPI, managed with [`uv`](https://docs.astral.sh/uv/)
- **Database**: PostgreSQL (Docker), SQLAlchemy as the ORM (no models yet)

## Project layout

```
.
├── docker-compose.yml
├── backend/
│   ├── pyproject.toml
│   ├── Dockerfile
│   ├── .env.example
│   └── app/
│       ├── main.py            # FastAPI app + CORS + health check
│       ├── core/
│       │   ├── config.py      # Settings (env vars via pydantic-settings)
│       │   └── database.py    # SQLAlchemy engine/session (no models yet)
│       ├── models/             # (empty) SQLAlchemy models go here
│       └── api/                 # (empty) routers go here
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        └── index.css
```

## Running it

### 1. Start Postgres (+ backend) with Docker

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

This brings up:
- `db` — Postgres 16, data persisted in a named volume, healthchecked
- `backend` — FastAPI on http://localhost:8000 (docs at `/docs`), auto-reloads on code changes

### 2. Run the frontend (separately, for fast dev reload)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on http://localhost:5173 and is already configured to proxy
`/api` requests to the backend at http://localhost:8000.

## What's deliberately NOT here yet

- No SQLAlchemy models / Alembic migrations
- No API routers/endpoints beyond `/health`
- No auth
- No frontend pages beyond a placeholder that pings `/health`

Next steps once you're ready: add SQLAlchemy models under `backend/app/models/`,
wire up Alembic for migrations, and start adding routers under `backend/app/api/`.
