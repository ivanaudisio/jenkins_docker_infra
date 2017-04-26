node (){
  stage('create Operation Center'){
    sh 'docker run -8888:8080 -d --name cjoc -h cjoc  cloudbees/jenkins-operations-center'
  }
  stage('create masters'){
    sh 'docker run -8001:8080 -d --name master01 --link cjoc:cjoc -h master01 cloudbees/jenkins-enterprise
    sh 'docker run -8002:8080 -d --name master02 --link cjoc:cjoc -h master02 cloudbees/jenkins-enterprise
  }
  stage('create shared-agents'){
    sh 'docker run -d -h slave1 --name slave1 --link cjoc:cjoc jenkins_slave'
    sh 'docker run -d -h slave2 --name slave2 --link cjoc:cjoc jenkins_slave'
  }
  stage('create agents'){
  
  }
}
