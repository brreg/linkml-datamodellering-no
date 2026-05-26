FROM python:3.11-slim AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local

# server.py, converter.py, validator.py og profiles/ vert montert inn ved køyring.
# Placeholders sikrar at CMD ikkje feilar ved bygg utan mount.
RUN touch server.py converter.py validator.py

RUN useradd -m mcp
USER mcp

CMD ["python", "server.py"]
