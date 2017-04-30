# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node.
FROM ubuntu:trusty
MAINTAINER Ivan Audisio

# In case you need proxy
#RUN echo 'Acquire::http::Proxy "http://127.0.0.1:8080";' >> /etc/apt/apt.conf

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
# installing wget & curl

# Copy slave.jar file for JNLP connection
COPY ./agent.py /home/jenkins/

RUN locale-gen en_US.UTF-8 &&\
    apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends openssh-server &&\
    apt-get -q autoremove &&\
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends openjdk-7-jre-headless &&\
    apt-get install curl -y &&\
    apt-get install wget -y &&\
    apt-get install python-mechanize -y &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set user jenkins to the image
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\
    echo "jenkins:jenkins" | chpasswd

# Standard SSH port
EXPOSE 22

# Default command
# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "/home/jenkins/agent.py"]
