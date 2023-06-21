#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.
# Create a fake HTML file with sample to test Nginx configuration
# Create a symbolic link. If the symbolic link already exists, it is deleted and recreated every time the script is ran.
# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive.
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# Restart nginx after updating the configuration.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "<html><head></head><body>My web page</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
