FROM python:3.6-alpine

COPY requirements.txt /tmp/

RUN apk add --no-cache --virtual .build-deps gcc musl-dev make postgresql-dev && \
    apk add --no-cache libpq && \
    pip install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt && \
    apk del .build-deps && \
    rm /tmp/requirements.txt && \
    mkdir /app

COPY --chown=1001 stats_service /app/stats_service

WORKDIR /app

USER 1001

CMD ["python", "-m", "stats_service"]