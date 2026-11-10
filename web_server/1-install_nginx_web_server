#!/usr/bin/env bash
# Installs nginx on the server and makes it serve "Holberton School for the win!" on port 80
sudo apt-get update -y
sudo apt-get install nginx -y
echo "Holberton School for the win!" | sudo tee /var/www/html/index.html
sudo service nginx restart
