#!/usr/bin/env bash
set -o errexit
set -o pipefail

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Apply migrations and gather static assets for production
python manage.py migrate --noinput
python manage.py collectstatic --noinput || echo "collectstatic skipped (STATIC_ROOT not configured)"
