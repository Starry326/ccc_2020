FROM python:latest
MAINTAINER zilongd@student.unimelb.edu.au
COPY ./app/ /app/
WORKDIR /app/
RUN pip install flask flask_restful pycurl couchdb tweepy
EXPOSE 5000
CMD ["python","flaskPart.py"]