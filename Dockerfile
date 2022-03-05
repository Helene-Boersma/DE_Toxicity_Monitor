FROM python:3.8

WORKDIR /code

ENV FLASK_APP=app_flask.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install pytest
RUN pip install selenium

EXPOSE 5000

COPY . .

CMD ["flask", "run"]
