#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

echo "-> Run unittests"

python -m tox -c timeseries_service
python -m tox -c stats_service

echo "-> Building Docker images"

docker build --no-cache -t timeseries_service:dev -f timeseries_service/Dockerfile timeseries_service
docker build --no-cache -t stats_service:dev -f stats_service/Dockerfile stats_service

echo "-> Run Docker Compose"

docker-compose up -d

sleep 5

echo "-> Run acceptance tests"

python -m robot atests
