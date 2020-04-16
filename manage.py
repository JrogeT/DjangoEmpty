#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#pip install django
#pip install django=1.0.0
#django-admin startproject mysite
#python manage.py startapp polls
#python manage.py runserver
#python manage.py runserver <port>
#python manage.py migrate
#python manage.py createsuperuser

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoempty.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
