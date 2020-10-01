

FROM python:2.7
ADD Flask.py /
ADD requirements.txt /
RUN pip install flask
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5001 
CMD ["python","Flask.py"]
