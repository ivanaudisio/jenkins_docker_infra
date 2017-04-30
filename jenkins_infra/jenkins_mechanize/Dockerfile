# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node.
FROM ubuntu
MAINTAINER Ivan Audisio

RUN apt-get update && \
    apt-get install python-mechanize -y && \
    apt-get install default-jdk -y && \
    apt-get install wget -y

COPY ./attach.master.groovy /home/
COPY ./configure.jenkins.infra.py /home/
COPY ./shared-agent.xml /home/

# Default command
CMD ["python", "/home/configure.jenkins.infra.py"]
