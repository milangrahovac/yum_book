targets help: ## List all targets with short descriptions.
	@echo "List of all targets:"
	@len=$$(grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F ':.*?## ' '{print length($$1)}' | sort -nr | head -n1); \
	grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk -v len=$$((len+1)) -F ':.*?## ' '{ printf "%-*s - %s \n", len, $$1, $$2 }' | sort

stop: ## Stop the server on port 8000.
	sh stop_server.sh

run: stop ## Stop server on port 8000 if running then run django server on port 8000.
	sleep 1
	python3 manage.py runserver

requirements: ## Install requirements.
	pip3 install -r requirements.txt

migrate: ## Applying database migrations.
	python3 manage.py makemigrations
	sleep 1
	python3 manage.py migrate


