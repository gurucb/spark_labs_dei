# Step-by-Step Guide to Create a Running Spark Cluster with Docker Compose
## Prerequisites
1. Docker: Ensure Docker is installed on your machine. You can download it from Docker's official website.
2. Docker Compose: Ensure Docker Compose is installed. It usually comes with Docker Desktop, but you can also install it separately by following the instructions on Docker Compose's official website.
## Docker Compose File
Here is an example docker-compose.yml file for setting up a Spark cluster:
```
*        `version: '3.8'
        services:
        spark-master:
            image: bitnami/spark:latest
            container_name: spark-master
            environment:
            - SPARK_MODE=master
            - SPARK_RPC_AUTHENTICATION_ENABLED=no
            - SPARK_RPC_ENCRYPTION_ENABLED=no
            - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
            - SPARK_SSL_ENABLED=no
            ports:
            - "8080:8080"
            - "7077:7077"

        spark-worker-1:
            image: bitnami/spark:latest
            container_name: spark-worker-1
            environment:
            - SPARK_MODE=worker
            - SPARK_MASTER_URL=spark://spark-master:7077
            - SPARK_WORKER_MEMORY=1G
            - SPARK_WORKER_CORES=1
            depends_on:
            - spark-master

        spark-worker-2:
            image: bitnami/spark:latest
            container_name: spark-worker-2
            environment:
            - SPARK_MODE=worker
            - SPARK_MASTER_URL=spark://spark-master:7077
            - SPARK_WORKER_MEMORY=1G
            - SPARK_WORKER_CORES=1
            depends_on:
            - spark-master
*```