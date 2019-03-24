import jenkins
import sys
#Etoro - Interview exercise. hopfully will get them to hire me....
#Created by Haimke
#18.3.2019

Script_Success_Index = sys.argv[3]
counter = sys.argv[2]
if counter % Script_Success_Index == 0:
    server = jenkins.Jenkins('http://localhost:8080/', username='haim', password='Tempo20192019!')
    job_name = server.get_job_name(sys.argv[1])
    print ("Job name is: ", job_name)
    sys.exit(0)
else:
    sys.exit(1)



