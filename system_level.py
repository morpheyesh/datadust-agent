import os
import re
import string
import subprocess
import platform
import sys

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
       
       itemR= re.compile(r'.*?\s+(\d+)[\s+]?')
       valueR = re.compile(r'\d+\.\d+')  
       headR = re.compile(r'.*?([%][a-zA-Z0-9]+)[\s+]?') 
       proc = None
       
       try:
          proc = subprocess.Popen(['mpstat', '-P', 'ALL', '1', '1'], stdout=subprocess.PIPE)
          
          mpstat = proc.communicate()[0]
          print "----"
          print mpstat
          if int(current_python[1]) >= 6:
              try:
                  proc.kill()
              except:
                  print "proc is dead already! "
          
              mpstat = mpstat.split('\n')
              mpstat.pop(1)      
              head = mpstat[1]
              headName = re.findall(headR, head)
              
              #take each line out
               
              for singleLine in range (2, len(mpstat)):
                  singleIndex =  mpstat[singleLine]
                  
                  if not singleIndex:
                      break
                  
                  device = re.match(itemR, singleIndex)
                 
                  if string.find(singleIndex, 'all') is not -1:
                      ndevice = 'ALL'
                  elif device is not None:
                      ndevice = 'CPU%s' % device.groups()[0]
                      
                  values = re.findall(valueR, singleIndex.replace(',','.'))
                  
                  stats[ndevice] = {}
                  
                  for headerIndex in range(0, len(headName)):
                      headNames = headName[headerIndex]
                      stats[ndevice][headNames] = values[headerIndex]
              

       except OSError:
          return false
      
    else:
        print 'Different platform!'
        return False

    print 'Done!'
    print stats
    return stats






















