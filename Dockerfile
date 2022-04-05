FROM python:3.8-slim-buster

WORKDIR /flask-todo

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]