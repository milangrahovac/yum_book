## Deploying Yum Book Django App on Minikube with Argo CD

✅ Prerequisites
- Minikube installed
- kubectl installed
- Helm installed

1. Start Minikube. 
```
minikube start
```

2. Install Argo CD.
```
kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml 
```
3.  Wait ~30 seconds until all Argo CD pods are running: <br>
```
kubectl get pods -n argocd
```

4.  🔐 Get Argo CD Initial Password
```
kubectl get secret argocd-initial-admin-secret -n argocd \
  -o jsonpath="{.data.password}" | base64 -d && echo
```

5. Access Argo CD UI
- Forward the Argo CD API server locally:
```
kubectl port-forward -n argocd svc/argocd-server 8080:443
```
Then open your browser and visit:
```
http://localhost:8080
```
Log in to ArgoCD UI using:

- Username: admin
- Password: (from step 4)

6. 📦 Deploy the Application
The Argo CD Application manifest at argocd/yum-book-app.yaml.
```
kubectl apply -f argocd/yum-book-app.yaml
```
This will create a new Application in Argo CD, which pulls your Helm chart and deploys the Django app.

7. Monitor progress in the Argo CD UI until the app shows Healthy and Synced. Then expose the service from Minikube:
```
minikube service yum-book-service -n yum-book
```
This command will open your Django app in the browser via a local Minikube tunnel. <br><br><br>


🧼 Optional Cleanup
To delete everything:
```
minikube delete
```