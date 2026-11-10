#!/usr/bin/env bash
# Installs nginx, serves the page, and adds a 301 redirect from /redirect_me
sudo apt-get update -y
sudo apt-get install nginx -y
echo "Holberton School for the win!" | sudo tee /var/www/html/index.html
sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default
sudo service nginx restart
