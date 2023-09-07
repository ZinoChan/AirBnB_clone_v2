#!/usr/bin/env bash
# set up nginx

apt update -y
apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head></head>
  <body>
    Nginx test page!
  </body>
</html>" | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

location="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo sed -i "/server_name _;/a $location" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
