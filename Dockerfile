# Zvanična Python slika
FROM python:3.11-slim

# Onemogućava Python da pravi .pyc fajlove i primorava direktan ispis u konzolu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Postavljanje radnog foldera u kontejneru
WORKDIR /app

# Kopiranje fajlova sa zavisnostima
COPY requirements.txt /app/

# Instalacija paketa (Django, Gunicorn, itd.)
RUN pip install --no-cache-dir -r requirements.txt

# Kopiranje celog projekta u kontejner
COPY . /app/