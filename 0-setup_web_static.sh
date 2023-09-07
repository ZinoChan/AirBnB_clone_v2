#!/usr/bin/python3
# set up nginx

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head></head>
  <body>
    Nginx test page!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

location="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo sed -i "/server_name _;/a $location" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
