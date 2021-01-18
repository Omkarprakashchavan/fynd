1. Created app.py file to run flask application
2. Requirement.txt file contains dependency for python application
3. Dockerfile created for containerizing the python flask application
4. Deployment.yaml and service.yaml created to deploy the application in Kubernetes cluster
5. To deploy the application in default namespace run below command:
	Kubectl apply -f deployment.yaml
6. To deploy the service in default namespace run below command:
	Kubectl apply -f service.yaml
7. Create ingres in default namespace run below command:
	Kubectl apply -f ingress.yaml
8. Similarly run below commands to create deployment, service and ingres in another namespace:
Kubectl apply -f deployment.yaml -n app-ns
Kubectl apply -f service.yaml -n app-ns
Kubectl apply -f ingress.yaml -n app-ns
