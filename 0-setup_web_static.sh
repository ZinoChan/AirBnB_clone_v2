#!/usr/bin/env bash
# Installs Nginx, listening on port 80

apt-get update
apt-get -y install nginx


mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

echo -e "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
	index index.nginx-debian.html;
    location /hbnb_static {
        alias /data/web_static/current;
		index index.nginx-debian.html;
    }
    location /redirect_me {
        return 301 https://en.wikipedia.org/wiki/Nginx;
    }
	error_page 404 /error_404.html;
	location /404 {
		root /etc/html;
		internal;
    }
}" > /etc/nginx/sites-available/default

sudo ln -fs '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'


sudo service nginx restart
