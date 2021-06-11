FROM python:3.9-alpine

ENV FLASK_APP=api.py
ENV FLASK_ENV=development

EXPOSE 5000

RUN pip install flask

WORKDIR /usr/src/api

CMD [ "flask", "run", "--host=0.0.0.0" ]
