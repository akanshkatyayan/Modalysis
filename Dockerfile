FROM python:3.7.4
WORKDIR /Modalysis
COPY . /Modalysis
RUN pip install -r requirements.txt 
EXPOSE 5000 
CMD ["python" , "wsgi.py"]