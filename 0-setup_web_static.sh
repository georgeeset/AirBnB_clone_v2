#!/usr/bin/env bash
# install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folder /data/web_static/releases/test/ if it doesn't exist
sudo mkdir -p /data/web_static/releases/test

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# give ownership to user and group
sudo chown --recursive ubuntu:ubuntu /data
# Create a fake HTML file /data/web_static/releases/test/index.html

sudo echo "Hello ALX SE" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current
# linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
sudo sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default

# apply last setings and restart nginx
sudo ufw allow "Nginx HTTP"
sudo service nginx restart
exit 0
