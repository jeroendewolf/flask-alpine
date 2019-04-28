FROM python:3-alpine
EXPOSE 5000
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python app.py
