sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf
sudo service nginx restart

cd /home/box/web/ask
gunicorn ask.wsgi:application --bind 0.0.0.0:8000
