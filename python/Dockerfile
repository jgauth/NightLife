FROM python:3.7

WORKDIR /usr/local/john
COPY ./wait_for_it.sh /wait_for_it.sh
RUN chmod +x /wait_for_it.sh

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

CMD ["/wait_for_it.sh", "db:5432", "--","python","-m","flask","run", "--host=0.0.0.0"]
