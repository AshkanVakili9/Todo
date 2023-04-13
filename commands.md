py -m venv venv

pip install -r req.txt

py manage.py makemigrations

py manage.py migrate

create .env

py manage.py shell

from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
