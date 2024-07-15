FROM python:3.12-slim


WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends

RUN python3 -m venv /opt/venv

COPY pyproject.toml ./

COPY panel-lemanique-db/ /app

RUN pip install .[dev]
