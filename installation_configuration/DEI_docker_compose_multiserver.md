# Step-by-Step Guide to Create a Running Spark Cluster with Docker Compose
## Prerequisites
1. Docker: Ensure Docker Desktop is installed on your machine. You can download it from Docker's official website.
2. ONLY on Windows Machine, enable WSL2. Refer[WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).
3. Docker Compose: Ensure Docker Compose is installed. It usually comes with Docker Desktop, but you can also install it separately by following the instructions on Docker Compose's official website.

## Docker Compose File
Docker-compose file is here [docker-compose](https://) https://github.com/gurucb/spark_labs_dei/blob/main/installation_configuration/DEI_docker_compose_multiserver.md for setting up spark cluster.
## Steps to Execute Docker Compose
1. Clone from git repo [Spark Labs](https://github.com/gurucb/spark_labs_dei) to local folder
2. Browse to folder that contains DEI_docker_compose_multiserver.yaml. Try to create a separate docker-compose.yaml file by reviewing content.
3. Start the Spark Cluster: Run the following command to start the Spark cluster:
```console
docker-compose -f DEI_docker_compose_multiserver.yaml up
```
4. Verify the Cluster:
Spark Master UI: Open your web browser and go to http://localhost:8080 to access the Spark Master UI.