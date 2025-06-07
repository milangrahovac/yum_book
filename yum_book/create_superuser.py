import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yum_book.settings')  # your settings module
django.setup()

# create_superuser.py
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'yumpass')
