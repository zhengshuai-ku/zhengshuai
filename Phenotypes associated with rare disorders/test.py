import os
import subprocess

for i in os.listdir(os.getcwd()):
    if i.endswith('xml'):
        try:
            cmd = "head -n 5 " + i + " | grep 'count'" 
            res = subprocess.check_output(cmd,shell = True ).split('"')[-2]
            print i, res
        except:
            print '----->', i, 'do not display a count of objects'
