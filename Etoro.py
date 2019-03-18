import jenkins
import sys
#Etoro - Interview exercise. hopfully will get them to hire me....
#Created by Haimke
#18.3.2019

server = jenkins.Jenkins('http://localhost:8080/jenkins/', username='haim', password='Tempo20192019!')
user = server.get_whoami()

version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
jobs = server.get_job_info(sys.argv[1],0,True)


build_info = server.get_build_info(sys.argv[1],int(sys.argv[2]))

duration = build_info["duration"]
status = build_info["result"]
print("Status: ",status)
print("Duration(ms): ",duration)



