#!/usr/bin/env bash
# Installs nginx with a redirect and a custom 404 page containing "Ceci n'est pas une page"
sudo apt-get update -y
sudo apt-get install nginx -y
echo "Holberton School for the win!" | sudo tee /var/www/html/index.html
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;\n\terror_page 404 \/404.html;/" /etc/nginx/sites-available/default
sudo service nginx restart
