FROM oliveiradigital/django-base:3.6-alpine

LABEL maintainer="Gabriel Oliveira <admin@oliveiradigital.com.br>"

COPY . /app

WORKDIR /app
RUN . .venv/bin/activate && \
    pip install -U pip && \
    pip install -r /app/requirements.txt

CMD ["/app/.venv/bin/uwsgi --chdir=/app --module=bootstrap.wsgi:application --master --processes 4 --threads 2 --chunked-input-timeout 3600 --harakiri 3600 --http11-socket :80"]

EXPOSE 80
