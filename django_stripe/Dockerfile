FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir --upgrade pip

COPY . .

CMD gunicorn django_stripe.wsgi:application --bind 0.0.0.0:8000