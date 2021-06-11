# docker-python-api

This repository implements a showcase how to run a Python Flask Web App in a Docker container.

An example web app (see api.py) is mounted (not copied) in the Docker container. When running
Flask in debug mode (FLASK_ENV=development) the app is relading upon code changes.

## Run Default Docker Image

```
docker run --rm --name python-api-runtime \
            -p 5001:5000 -e FLASK_APP=api.py -e FLASK_ENV=development \
            -v "$PWD":/usr/src/api -w /usr/src/api python:3.9-alpine \
            sh -l -c "pip install flask; flask run --host 0.0.0.0"
```

## Build Own Docker Image

```
docker build -t python-flask .

docker run --rm --name python-api-runtime -p 5001:5000 -v "$PWD":/usr/src/api python-flask
```
