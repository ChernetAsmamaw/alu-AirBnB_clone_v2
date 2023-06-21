#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create the following folders if they don’t already exist:
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file with sample to test Nginx configuration
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@5419-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link. If the symbolic link already exists, it is deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart nginx after updating the configuration.
sudo service nginx restart
