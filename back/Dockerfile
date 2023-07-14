# DOCKERFILE API

FROM python:3.9-slim

WORKDIR /code/back


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY requirements.txt ./

# Cache dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt --progress-bar off

# Copy source code
COPY . /code/back

ENTRYPOINT ["sh", "entry.sh"]

