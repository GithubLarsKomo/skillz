FROM python:3.12-alpine

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SPORT_RUNTIME_HOST=0.0.0.0
ENV SPORT_RUNTIME_PORT=8080
ARG SKILLZ_REVISION=unknown
ENV SKILLZ_REVISION=${SKILLZ_REVISION}

COPY scripts ./scripts
COPY skills ./skills
COPY schemas ./schemas

RUN addgroup -S skillz && adduser -S -G skillz skillz && chown -R skillz:skillz /app
USER skillz

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD ["python", "-c", "import os,urllib.request; urllib.request.urlopen('http://127.0.0.1:'+os.environ.get('SPORT_RUNTIME_PORT','8080')+'/healthz', timeout=3).read()"]
CMD ["python", "scripts/serve_sport_specialist_runtime.py"]
