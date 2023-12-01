FROM debian:12-slim
COPY ./app /app

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cach-dir -r /app/requirements.txt

ENTRYPOINT qunicorn main:app --bind 0.0.0.0:5000
