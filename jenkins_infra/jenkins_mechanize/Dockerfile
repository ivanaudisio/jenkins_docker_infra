FROM ubuntu
MAINTAINER Ivan Audisio

RUN apt-get -q update &&\
    apt-get install default-jdk -y &&\
    apt-get install wget -y &&\
    apt-get install python-mechanize -y &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

COPY ./attach.master.groovy /home/
COPY ./configure.jenkins.infra.py /home/
COPY ./shared-agent-01.xml /home/

# Default command
CMD ["python", "/home/configure.jenkins.infra.py"]
