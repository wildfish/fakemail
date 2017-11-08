FROM python:2.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    curl \
    wget \
    time \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone git@github.com:wildfish/fakemail.git /app

CMD ["python", "/app/server.py"]
