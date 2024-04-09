FROM debian:latest

LABEL author="LZI"
LABEL description="DockerApp"
LABEL version="1.0"

RUN apt-get update && apt-get install -y nginx

EXPOSE 80/tcp

CMD [ "nginx", "-g", "daemon off;" ]