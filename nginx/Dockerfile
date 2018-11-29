FROM nginx:alpine
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/perfect-forward-secrecy.conf /etc/nginx/perfect-forward-secrecy.conf
COPY ./nginx/dh4096.pem /etc/nginx/dh4096.pem
USER root
RUN mkdir -p /usr/local/src/john

COPY ./frontend/ /usr/local/src/john/
EXPOSE 80 443
