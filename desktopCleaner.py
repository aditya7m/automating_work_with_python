
# This code can be run as it is (just run it) on any Debian based distro.
# But it can also be used to run on any other Operating System by just
# changing the mypath variable to your desired folder which you want to
# clean up.

import os
import shutil
from os.path import isfile, join
mypath = '/home/<user-name>/Desktop'
os.chdir(mypath)
print(os.listdir('.'))
files = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
for file in files:
    if file[0] == '.':
        continue
    li = list(file.split('.'))
    folder_name = li[-1]
    try:
        os.mkdir(join(mypath, folder_name))
    except FileExistsError:
        pass
    try:
        shutil.move(join(mypath, file), join(mypath, folder_name))
    except shutil.Error:
        pass
print(os.listdir('.'))
