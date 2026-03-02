FROM python:3.11-slim

ARG VERSION="1.0"
ARG BUILD_DATE="01/03/2026"
ARG REQUIREMENTS="requirements.txt"

LABEL org.opencontainers.authors="LEFKI MEIDI,MELINA KERNOU,BADREDINE BOUAMAMA"
LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.created=${BUILD_DATE}
LABEL org.opencontainers.description="TP à rendre"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ${REQUIREMENTS} .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r ${REQUIREMENTS}

COPY . .

CMD ["python", "evaluate.py"]
