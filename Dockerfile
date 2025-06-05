FROM python:3.12.6-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create admin user
RUN echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', '', 'yumpass')" \
    | python manage.py shell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
