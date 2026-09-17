FROM python:3.12-slim

# Install uv (fast Python package/dependency manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency manifests first for better layer caching
COPY pyproject.toml ./

# Install dependencies (no project code yet, just deps) into a local .venv
RUN uv sync --no-install-project

# Copy the rest of the app
COPY . .

# Sync again to install the project itself
RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
