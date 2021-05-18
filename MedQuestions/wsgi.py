"""
WSGI config for MedQuestions project.
# wsgi.py
# Created by Egor Matveev
# 16.05.2021
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedQuestions.settings')

application = get_wsgi_application()
