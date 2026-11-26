
FROM python:3.11-slim AS builder

ENV PIP_DEFAULT_TIMEOUT=120 \
    PIP_RETRIES=10 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

COPY requirements.txt .

RUN python -m pip install \
    --no-cache-dir \
    --require-hashes \
    --only-binary=:all: \
    --target=/install \
    -r requirements.txt


FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/install \
    APP_ENV=production

WORKDIR /app

RUN apt-get update \
    && apt-get install --only-upgrade -y --no-install-recommends libzstd1 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --system appgroup \
    && useradd --system --gid appgroup --no-create-home appuser \
    && rm -rf /usr/local/lib/python3.11/site-packages/setuptools \
              /usr/local/lib/python3.11/site-packages/setuptools-*.dist-info

COPY --from=builder /install /install

COPY --chown=appuser:appgroup app/ ./app/

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=10s \
            --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
