############################################################
# Dockerfile
# Install latest Jenkins
############################################################
FROM cloudbees/jenkins-operations-center:1.625.24.1
MAINTAINER ivan.audisio

COPY config_cjoc.groovy /usr/share/jenkins/ref/init.groovy.d/config_cjoc.groovy

# Create Jenkins Log Folder
#USER root
#RUN mkdir /var/log/jenkins
#RUN chown -R jenkins:jenkins /var/log/jenkins
#USER jenkins

#USER jenkins

#ENV JAVA_OPTS="-Xmx8192m"
#ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300"

# Install vim to modify files
# Restore basic bash commands like top, less, more, clear

#USER root
#RUN apt-get -y update && \
#    apt-get install -y vim && \
#    export TERM=xterm && \
#    echo export TERM=xterm >> /root/.bashrc
#USER jenkins

# Set default options
#ENV JAVA_OPTS="-Xmx8192m"
#ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300 --logfile=/var/log/jenkins/jenkins.log"

EXPOSE 8080

#CMD ["tail", "-f", "/dev/null"]
