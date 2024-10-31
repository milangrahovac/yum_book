stop:
	sh stop_server.sh

run: stop
	sleep 1
	python3 manage.py runserver

create_requirements:
	pip3 freeze > requirements.txt

install_requirements:
	pip3 install -r requirements.txt

migrate:
	python3 manage.py makemigrations
	sleep 1
	python3 manage.py migrate

up: stop
	sleep 1
	docker-compose up

down:
	docker-compose down
	sleep 1
	sh stop_server.sh


# python3 manage.py collectstatic