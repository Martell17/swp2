


sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/guni.conf
sudo service nginx restart

sudo ln -s /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
cd /home/box/web/
gunicorn -c /etc/gunicorn.d/hello.py hello:app

