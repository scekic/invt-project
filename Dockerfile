FROM python:3.12-slim-bullseye

RUN apt-get update && apt-get -y install libpq-dev gcc g++ curl procps net-tools tini

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"


ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app/

RUN /root/.cargo/bin/uv venv /opt/venv && \
    /root/.cargo/bin/uv pip install --no-cache -r /app/requirements.lock

EXPOSE 8000