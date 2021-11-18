#docker build . -t homework-03 && docker run -d --name homework-03 -p 8000:8000 homework-03
FROM python:3.9-buster

WORKDIR /opt/application

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY application .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app:app", "--host=0.0.0.0"]
