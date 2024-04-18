FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN pip install -r requirements.txt --upgrade --no-cache-dir

COPY .env /app
COPY . /app

CMD ["gunicorn", "color_palettes.wsgi:application", "--bind", "0:8000" ]
