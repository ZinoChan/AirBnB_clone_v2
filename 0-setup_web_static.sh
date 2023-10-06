!/usr/bin/env bash
# Installs Nginx, listening on port 80

apt-get update
apt-get -y install nginx


# Incoming HTTP fix
sudo ufw allow 'Nginx HTTP'


sudo chmod -R 755 /var/www

sudo mkdir /data/
sudo chown -hR ubuntu /data/
sudo chgrp -hR ubuntu /data/


# Creating directories and pages
sudo mkdir -p /var/www/html/ /var/www/error
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo touch /var/www/html/index.nginx-debian.html


sudo rm -fr /data/web_static/current

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current



# Adding the string
echo 'Holberton School' > /var/www/html/index.nginx-debian.html

# Setting up a custom 404 page message
echo -e "Ceci n'est pas une page" > /var/www/html/error_404.html

echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html


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
