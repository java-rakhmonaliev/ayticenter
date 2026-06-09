#!/bin/bash
apt-get update -y
apt-get install -y python3-pip python3-venv nginx git postgresql-client nodejs npm

git clone https://github.com/java-rakhmonaliev/ayticenter.git /app
cd /app

# Build Tailwind CSS
npm install
npm run build:css

# Python env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cat > /app/.env << 'EOF'
SECRET_KEY=${secret_key}
DEBUG=False
ALLOWED_HOSTS=aytimarkaz.uz,www.aytimarkaz.uz
DB_NAME=aytimarkaz
DB_USER=aytimarkaz_user
DB_PASSWORD=${db_password}
DB_HOST=${db_host}
DB_PORT=5432
SECURE_SSL_REDIRECT=False
DJANGO_SETTINGS_MODULE=config.settings.prod
EOF

source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=config.settings.prod
python manage.py migrate
python manage.py collectstatic --noinput

tee /etc/systemd/system/aytimarkaz.service << 'EOF'
[Unit]
Description=AyTi Markaz Django App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/app
EnvironmentFile=/app/.env
ExecStart=/app/.venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:8000 --workers 2
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable aytimarkaz
systemctl start aytimarkaz

tee /etc/nginx/sites-available/aytimarkaz << 'EOF'
server {
    listen 80;
    server_name aytimarkaz.uz www.aytimarkaz.uz;

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
EOF

ln -s /etc/nginx/sites-available/aytimarkaz /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx