sudo cp docker-compose_online.yml docker-compose.yml
sudo cp nginx/nginx_online.conf nginx/nginx.conf
sudo docker-compose build
sudo docker-compose up -d
