FROM python:3

WORKDIR /flask-todo

COPY . .

RUN pip install -r requirements.txt

# CMD python app.py
CMD gunicorn --bind 0.0.0.0:5000 -w 3 app:app