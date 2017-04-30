import jenkins.model.*
import jenkins.*
import hudson.model.*
import hudson.*

Jenkins.instance.setNumExecutors(0)

Jenkins.instance.setSlaveAgentPort(50000)

configuration = JenkinsLocationConfiguration.get().setUrl('http://jenkins:8080')
configuration.save()
