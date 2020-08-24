# Crypto World

Containerized web-app, using flask microframework and configured to run with `gunicorn`.

## Build image && run container

```bash
GUNICORN_PORT='80' # in which port is gunicorn running
GUNICORN_WORKERS='2' # How many workers has gunicorn
DOCKER_TAG='crypto:latest'
docker build --tag ${DOCKER_TAG} \
    --build-arg PORT=${GUNICORN_PORT} \
    --build-arg WORKERS=${GUNICORN_WORKERS} .
```

## Running the container

### Development

```bash
# Use  virtual environment
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

```bash
GUNICORN_PORT='8000'
DOCKER_TAG='crypto:latest'
DOCKER_NAME='crypto'
docker run -tid -p ${GUNICORN_PORT}:${GUNICORN_PORT} -v $(pwd):/app \
--name ${DOCKER_NAME} ${DOCKER_TAG}
```
