#!/bin/bash
set -e

echo "codewithmuh-backend:boot:env:${APP_ENVIRONMENT}"

python manage.py migrate
python manage.py collectstatic --noinput
