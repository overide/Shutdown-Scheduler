#---------------------------------------------------------------------
#Name      : Shutdown Scheduler
#Purpose   : Automatically shutdown your system after specified hours!
#Author    : Atul Kumar
#Created   : 24/06/2016
#---------------------------------------------------------------------

import subprocess
import datetime

def shutdown():
	subprocess.call(["shutdown","/s","/f","/t","30","/c","You'r using computer too much,take rest buddy, breathe!"])
	sys.exit()
	
print("System started!")
sys_start_time=datetime.datetime.now()
sys_maxhour=8 #set your hours
tmp=datetime.timedelta(hours=sys_maxhour)
sys_shutd_time=tmp+sys_start_time
while True:
	ct=datetime.datetime.now()
	if(ct>=sys_shutd_time):
		shutdown()