# Docker_Tutorial
This repo has content about Docker

Create virtual environment using below command:
```
Adding virtual env : python -m venv ./venv
Actiavting virtual env : .\venv\Scripts\Activate.ps1
```
Command to build docker image
```
docker build -t welcome-app .
```
Check docker images
```
docker images
```
Run the docker images - Hostname mapping
```
docker run -p 5000:5000 welcome-app
```
Two IPs: 
```
http://172.0.0.1:5000 -- It is wrt localhost and it will run normally
http://172.17.0.2:5000 -- It will not run initially. It is the IP present in the ocntainer. We can access it through our host container thorugh specific port
```
Command to check how many container is running
```
docker ps
```
Command to stop the container
```
docker stop "container_id"
```

Steps for docker hub deployment:
Command to docker login
```
docker login
```
* Then provide username and password

Command to rename the docker app name:
1st way:
Command to remove docker image
```
docker image rm -f welcome-app
```
Command to build again
```
docker build -t hitterdixit/welcome-app .
```
2nd way:
Command to change the docker image name
```
docker tag hitterdixit/welcome-app hitterdixit/welcome-app1
```
* Naming convetion for docker hub should be username/docker_image_name
Command to push to docker hub repository
``` 
docker push hitterdixit/welcome-app:latest
```
* After that we can also download the image and run it as a container
Command to pull docker image from dockerhub
``` 
docker pull hitterdixit/welcome-app:latest
```

Docker compose:
```
It is a tool to run and define multi-conatainer docker application
```
docker-compose.yml file: It is used to tun multi-container docker application

EXPOSE variable: It is used to specifiy port number that will be exposed to container