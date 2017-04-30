import jenkins.model.*
import jenkins.*
import hudson.model.*
import hudson.*

Jenkins.instance.setSlaveAgentPort(50000)

configuration = JenkinsLocationConfiguration.get().setUrl('http://cjoc:8080')
configuration.save()
