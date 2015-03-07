#!/usr/bin/env python


import sys
import subprocess
import platform
import sched
import time

from system_level import system_level
from ddDaemon import Daemon

if (sys.version_info[1]) <= 6:
    print("Its recommended to use python version 2.7 or above. 2.7 is the best!")
    sys.exit(1)
    
ddConfig = {
        'version': '0.1.0',
        'interval': 60
           }

def no_of_cores():
    
    greppy = subprocess.Popen(['grep', 'cpu cores', '/proc/cpuinfo'], stdout=subprocess.PIPE, close_fds = True, shell = True)
    printLine = subprocess.Popen(['wc -l'], stdin=greppy.stdout, stdout=subprocess.PIPE, close_fds = True, shell = True)
    noOfCores = printLine.communicate()[0]
    
    return int(noOfCores)

class datadust_agent(Daemon):
    
   #def run(self): 
       
    BasicStats = {
            'processorType': platform.processor(),
            'noOfCores': no_of_cores(),
            'os': sys.platform,      
            'nixDist': platform.dist()   
                 } 
    #expand later when more dist support!(.) 
    
    
    #system_level instance 
    sysLevel = system_level(ddConfig) 
    schedule = sched.scheduler(time.time, time.sleep)
    sysLevel.system_levelChecks(schedule, True, BasicStats)  
    schedule.run()
    
    
if __name__ == '__main__':
      argL = len(sys.argv)
    #need to do logging - logFile(.)

      
      d = datadust_agent() #pids..(..)
      
      if argL == 2 or argL == 3 or argL == 4:
         if 'start' == sys.argv[1]:
            print("Started daemon..------------------------------------------------------")
            d.start()
         
         elif 'stop' == sys.argv[1]:
             print("Daemon stopped!")
             d.stop()
             
          
          
          
         else:
            print 'Check the commands properly!'
            sys.exit(1)

         sys.exit(0)

      else:
        print 'usage: %s start|stop|restart|status|update' % sys.argv[0]
        sys.exit(1)
    