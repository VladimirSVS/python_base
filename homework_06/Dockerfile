FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app