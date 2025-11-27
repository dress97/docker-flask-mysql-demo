FROM jenkins/jenkins:lts

USER root

# Instala docker CLI y docker-compose plugin (Debian/Ubuntu base)
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get install -y curl && \
    curl -L "https://github.com/docker/compose-plugin/releases/download/v2.21.0/docker-compose-linux-x86_64" -o /usr/local/lib/docker/cli-plugins/docker-compose && \
    chmod +x /usr/local/lib/docker/cli-plugins/docker-compose && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER jenkins
