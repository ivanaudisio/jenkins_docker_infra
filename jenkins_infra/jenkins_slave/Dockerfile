FROM ubuntu:trusty
MAINTAINER Ivan Audisio

RUN apt-get -q update &&\
    apt-get install default-jdk -y &&\
    apt-get install wget -y &&\
    apt-get install python-mechanize -y &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

COPY ./agent.py /home/jenkins/
COPY ./shared-agent.xml /home/jenkins/

CMD ["python", "/home/jenkins/agent.py"]
