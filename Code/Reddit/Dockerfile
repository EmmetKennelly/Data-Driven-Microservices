FROM python:2.7
ADD RedditStreamer.py /
ADD requirements.txt /
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install pandas 
EXPOSE 5001 
CMD ["python","RedditStreamer.py"]



