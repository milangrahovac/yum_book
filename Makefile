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

test: ## Run tests.
	python3 manage.py test

# Variables (you can edit these)
IMAGE_NAME=yum-book
IMAGE_TAG=latest
DOCKER_USER=mgrah

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

# Tag the image for Docker Hub
tag:
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_TAG)

# Push the image to Docker Hub
push: build tag
	docker push $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_TAG)

# Build + tag + push in one command
all: build tag push

.PHONY: clean-yum-app-cluster
build-cluster:
	kubectl apply -f kubernetes/yum-book-deployment.yaml
	kubectl apply -f kubernetes/yum-book-service.yaml
	sleep 5
	minikube service yum-book-service


.PHONY: clean-yum-app-cluster
clean-cluster:
	kubectl delete deployments -l app=yum-book
	kubectl delete services -l app=yum-book