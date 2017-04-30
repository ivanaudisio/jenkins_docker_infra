import re
import time
from mechanize import Browser
import os # needed to execute shell commands - ex. os.system('ls')

max_retries=1000 # maximum number of times to retry
interval=5 # number of seconds to wait between retries
url="http://cjoc:8080/job/shared-agent-01" # URL to open
br = Browser()
br.set_handle_robots(False)
tried=0
connected = False

while not connected:
    try:
        response = br.open(url)
        connected = True # if line above fails, this is never executed
    except:
        print "connection could not be establish"
        time.sleep(interval)
        tried += 1
    if tried > max_retries:
        exit()

os.system('wget http://cjoc:8080/jnlpJars/jenkins-cli.jar')
os.system('wget http://cjoc:8080/jnlpJars/slave.jar')
os.system('java -jar slave.jar -jnlpUrl http://cjoc:8080/jnlpSharedSlaves/shared-agent-01/slave-agent.jnlp')
