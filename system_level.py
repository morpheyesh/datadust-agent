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

   for single in into_tuple:
      
        single = single.split()
        
        disk_usage.append(single)

   return disk_usage