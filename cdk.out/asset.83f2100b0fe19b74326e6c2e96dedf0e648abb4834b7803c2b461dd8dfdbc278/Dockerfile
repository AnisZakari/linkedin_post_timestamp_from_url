FROM python:3.11-slim-buster

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

CMD ["app.handler"]