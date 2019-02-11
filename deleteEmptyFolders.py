import os
from os.path import join, isdir
mypath = '/home/kunal/Desktop'
os.chdir(mypath)
print(os.listdir('.'))
for f in os.listdir(mypath):
    if isdir(join(mypath, f)):
        try:
            if not os.listdir(join(mypath, f)):
                os.rmdir(join(mypath, f))
        except PermissionError:
            pass
print(os.listdir('.'))
