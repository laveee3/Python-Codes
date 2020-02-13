import os, sys
from time import sleep
import time
import datetime

# run humidity_control_24hr_log.py to log data in logfile.csv every 24 hrs - done in crontab
# run a script that does the following every 24 hrs (after humidity_control_24hr_log.py script completes)
# 1 - rename log file
# 2 - email it with time stamp
# 3 - remove the file

#1
dt = str(datetime.date.today())
filename = 'humiditylog_'+ dt +'.csv'
filePath = '/home/pi/DHT22/' + filename
logfile = '/home/pi/DHT22/logfile.csv'
#print ("filename is " + filename + " logfile is " + logfile)
os.rename(logfile, filePath)

#2
emailCommand = 'python /home/pi/email_attach.py gdkps3@gmail.com HumidityLog_' +dt +' LastDaysLog ' + filename + ' ' +filePath
os.system(emailCommand)

#3
os.system('rm '+ filePath)
