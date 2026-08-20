FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml VERSION ./
COPY src ./src
RUN python -m pip install --upgrade pip && python -m pip install .

COPY docs ./docs
COPY skills ./skills
COPY schemas ./schemas
COPY contracts ./contracts

RUN adduser --disabled-password --gecos "" --uid 10001 skillz \
    && chown -R skillz:skillz /app
USER skillz

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3).read()" || exit 1

CMD ["skillz-mcp", "--repository-root", "/app", "--transport", "streamable-http", "--host", "0.0.0.0", "--port", "8000"]
