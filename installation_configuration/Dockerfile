FROM bitnami/spark AS jupyter-local 

#Copy Logging properties to all nodes of spark cluster
COPY        log4j2.properties /opt/bitnami/spark/conf/log4j2.properties
WORKDIR     /app
COPY        --chmod=777 app    /app/
RUN         pip install -r requirements.txt
EXPOSE      8888