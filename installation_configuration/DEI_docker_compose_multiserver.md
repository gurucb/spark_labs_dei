# Step-by-Step Guide to Create a Running Spark Cluster with Docker Compose
## Prerequisites
1. Docker: Ensure Docker Desktop is installed on your machine. You can download it from Docker's official website.
2. ONLY on Windows Machine, enable WSL2 and use default Ubuntu. Refer[WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).
3. Docker Compose: Ensure Docker Compose is installed. It usually comes with Docker Desktop, but you can also install it separately by following the instructions on Docker Compose's official website.

## Docker Compose File
Docker-compose YAML file [docker-compose](https://github.com/gurucb/spark_labs_dei/blob/gurucb/coding_samples/installation_configuration/DEI_docker_compose_multiserver.yaml) for setting up spark cluster.
## Steps to Execute Docker Compose
1. Clone from git repo [Spark Labs](https://github.com/gurucb/spark_labs_dei) to local folder
2. Browse to folder that contains DEI_docker_compose_multiserver.yaml.
3. To start Spark Cluster: Run the following command to start Spark cluster:
```console
docker-compose -f DEI_docker_compose_multiserver.yaml up
```
4. Verify the Cluster:
Spark Master UI: Open your web browser and go to http://localhost:8080 to access the Spark Master UI.
5. To build Spark cluster below files need to be present.
    1. Dockerfile
    2. DEI_docker_compose_multiserver.yaml
    3. .env
6. Additional Docker commands for debugging
```console
docker ps
docker images

docker run -it <imageid> /bin/bash
docker exec -it <containerid> -u 0 /bin/bash

docker network create <network Name> -d bridge

docker system df
docker builder prune --ll
```
