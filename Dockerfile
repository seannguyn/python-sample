FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir Flask

EXPOSE 80
CMD ["python", "python/main.py"]