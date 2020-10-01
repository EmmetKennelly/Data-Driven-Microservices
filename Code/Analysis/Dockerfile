FROM python:2.7-onbuild

ADD Tweets.py /
RUN pip install textblob
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080:5001 
CMD ["python", "Tweets.py"]
