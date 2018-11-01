FROM nginx:alpine
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
USER root
RUN mkdir -p /usr/local/src/john

COPY ./frontend/ /usr/local/src/john/
EXPOSE 80 443
