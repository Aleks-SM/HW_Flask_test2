FROM python:3.11-alpine
COPY ./app /app

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT qunicorn main:app --bind 0.0.0.0:5000
