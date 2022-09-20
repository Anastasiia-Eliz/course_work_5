FROM python:3.10

WORKDIR /code
COPY game/requirements.txt .
RUN pip install -r requirements.txt
COPY game .
ENV FLASK_APP=wsgi.py

CMD flask run -h 0.0.0.0 -p 80