# flask_helm

steps:
- build docker image
- docker login
- docker tag flask-demo-app:latest 2kunal6/your-app:latest
- sudo docker push 2kunal6/test-images:tagname
- try removing the compulsion to run docker with sudo:
  - sudo groupadd docker
  - sudo usermod -aG docker $USER
- minikube start
- helm install flask-demo-app flask-demo-app-chart
- access website: http://192.168.49.2:30000/ 
  - 'minikube ip' will give the above ip address

Notes:
- Docker volume: the docker volume uses the location from 'minikube host' not my actual machine host.  So the path provided in deployment.yaml (/home/docker) is the minikube host's path.
