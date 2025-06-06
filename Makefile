.PHONY: targets help
targets help: ## List all targets with short descriptions.
	@echo "List of all targets:"
	@len=$$(grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F ':.*?## ' '{print length($$1)}' | sort -nr | head -n1); \
	grep -E '^[\%\/\.0-9a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk -v len=$$((len+1)) -F ':.*?## ' '{ printf "%-*s - %s \n", len, $$1, $$2 }' | sort

.PHONY: stop
stop: ## Stop the server on port 8000.
	sh stop_server.sh

.PHONY: run
run: stop ## Stop server on port 8000 if running then run django server on port 8000.
	sleep 1
	python3 manage.py runserver

.PHONY: requirements
requirements: ## Install requirements.
	pip3 install -r requirements.txt

.PHONY: migrate
migrate: ## Applying database migrations.
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

.PHONY: build 
build: ## Build the Docker image.
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(DOCKER_USER)/$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: push
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
	kubectl delete deployments -l app=yum-book
	kubectl delete services -l app=yum-book
	kubectl delete -f kubernetes/yum-book-deployment.yaml
	kubectl delete -f kubernetes/yum-book-service.yaml
	
# minikube service yum-book-service -n yum-book
# kubectl port-forward -n argocd svc/argocd-server 8080:443


1. start minikube
minikube start

2. forward argo-cd port
kubectl port-forward -n argocd svc/argocd-server 8080:443

3.  kubectl apply -f argocd/helm.yaml