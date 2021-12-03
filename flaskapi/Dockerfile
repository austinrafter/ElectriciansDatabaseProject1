FROM python:3.9
WORKDIR /flaskapi

COPY requirements.txt  .flaskenv ./
RUN pip3 install -r ./requirements.txt
ENV FLASK_ENV production

EXPOSE 5000
COPY app.py models.py /flaskapi
CMD ["flask", "run", "--host=0.0.0.0"]
