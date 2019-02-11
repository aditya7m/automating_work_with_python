import os
import shutil
from os import listdir
from os.path import isfile, join
mypath = '/home/kunal/Desktop'
os.chdir(mypath)
print (os.listdir('.'))
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in files:
    li = list(file.split('.'))
    folder_name = li[-1]
    try:
        os.mkdir(join(mypath, folder_name))
    except FileExistsError:
        pass
    shutil.move(join(mypath, file), join(mypath, folder_name))
print (os.listdir('.'))
