DB_FILE = db.sqlite3

.PHONY: targets help
targets help: ## List all targets with short descriptions.
	@echo "List of all targets:"
	@len=$$(grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F ':.*?## ' '{print length($$1)}' | sort -nr | head -n1); \
	grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk -v len=$$((len+1)) -F ':.*?## ' '{ printf "%-*s - %s \n", len, $$1, $$2 }' | sort

.PHONY: run
run: stop requirements db ## Stop server on port 8000 if running then run django server on port 8000.
	python3 manage.py runserver

.PHONY: stop
stop: ## Stop the server on port 8000.
	sh stop_server.sh

.PHONY: requirements
requirements: ## Install requirements.
	pip3 install -r requirements.txt

.PHONY: db
db: ## Applying database migrations.
	sh create_dbsqlite3.sh
	sleep 1
	python3 manage.py makemigrations
	sleep 1
	python3 manage.py migrate

.PHONY: test
test: ## Run tests.
	python3 manage.py test

# Variables (you can edit these)
IMAGE_NAME=yum-book
IMAGE_TAG=latest
DOCKER_USER=mgrah

.PHONY: build-image
build: ## Build the Docker image.
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: push-image
push: build ## Push the image to Docker Hub.
	docker push $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: build-cluster
build-cluster: ## Build kubernetes cluster.
	kubectl apply -f kubernetes/yum-book-deployment.yaml
	kubectl apply -f kubernetes/yum-book-service.yaml
	sleep 5
	minikube service yum-book-service

.PHONY: clean-cluster
clean-cluster: ## clean kubernetes cluser.
	kubectl delete -f kubernetes/yum-book-deployment.yaml
	kubectl delete -f kubernetes/yum-book-service.yaml

.PHONY: argo
argo: ## build andrun argocd 
	kubectl create namespace argocd
	kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
