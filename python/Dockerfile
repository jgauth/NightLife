FROM python:3.7

WORKDIR /usr/local/john

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000
