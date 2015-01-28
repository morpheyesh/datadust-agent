import os
import re

import subprocess
import platform

current_python = platform.python_version_tuple()


class system_level:

 def __init__(self): #Explicit is better than implicit 
   print "Done Init-ing!"  
   
   
   
 def Disk_Util(self):
   disk_usage = []
   try:
     proc = subprocess.Popen(['df','-k'],stdout=subprocess.PIPE, shell=True)
     print proc
     command_exec = proc.communicate()[0]
     print command_exec
         
   
   except:
      print "Error! Cannot run commands"
      
   into_tuple = command_exec.split('\n')
   into_tuple.pop(0)                  

   for singleStat in into_tuple:
      
        singleStat = singleStat.split()
        
        disk_usage.append(singleStat)

   return disk_usage  

 def CPU_Stats(self):
     
     stats = {}
          
     if sys.platform == 'linux2':
       print "Good to go!"
       
       try:
          proc = subprocess.Popen(['mpstat', '-P', 'ALL', '1', '10'])
          mpstat = proc.communicate()
          
          if int(current_python[1]) >= 6:
              try:
                  proc.kill()
              except:
                  print "proc is dead already! "

      
       except:
          print "Something wrong in subprocess!"
          
          if int(current_python[1]) >= 6:
              try:
                  proc.kill()
              except:
                  print "proc is dead already! "

              
          
       mpstat = mpstat.split('/n')
       print mpstat      

























