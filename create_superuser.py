import os
import django

# Set the settings module for Django (must match your project)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yum_book.settings')

# Setup Django
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = 'admin'
    email = ''
    password = 'yumpass'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created.")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    create_superuser()



# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yum_book.settings')  # your settings module
# django.setup()

# # create_superuser.py
# from django.contrib.auth import get_user_model
# User = get_user_model()
# if not User.objects.filter(username='admin').exists():
#     User.objects.create_superuser('admin', '', 'yumpass')
