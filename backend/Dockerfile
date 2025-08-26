FROM python:3.12-slim

WORKDIR /app

# Copy the whole repo (or minimal files). Using context '.' ensures /app/backend exists
COPY . /app

# Install backend requirements (path relative to repo root)
RUN pip install --no-cache-dir -r backend/requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
