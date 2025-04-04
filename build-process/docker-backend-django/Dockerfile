FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=backend.settings

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git-core \
        build-essential \
        binutils \
        libproj-dev \
        gdal-bin \
        supervisor && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements /home/codewithmuh-backend/requirements
RUN mkdir -p /home/codewithmuh-backend/media
WORKDIR /home/codewithmuh-backend


RUN pip install --upgrade pip
RUN pip install -r ./requirements/requirements.txt



EXPOSE 8080

RUN mkdir -p /var/logs/codewithmuh


COPY ./ /home/codewithmuh-backend



CMD ["gunicorn", "--workers", "4", "--timeout", "120", "--bind", "0.0.0.0:80", "backend.wsgi:application"]


