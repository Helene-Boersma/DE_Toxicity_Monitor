FROM python:3.8

WORKDIR /code

ENV FLASK_APP=app_flask.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install pytest
RUN pip install selenium
RUN pip install pandas

EXPOSE 5000
EXPOSE 8010

COPY . .

CMD ["flask", "run"]
