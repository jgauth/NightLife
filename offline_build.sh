sudo cp docker-compose_offline.yml docker-compose.yml
sudo cp nginx/nginx_offline.conf nginx/nginx.conf
sudo docker-compose build
sudo docker-compose up
