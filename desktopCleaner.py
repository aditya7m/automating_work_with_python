
# This code can be run as it is (just run it) on any Debian based distro.
# But it can also be used to run on any other Operating System by just
# changing the mypath variable to your desired folder which you want to
# clean up.

# It's not a plain desktop cleaner, what it does is it checks for the file
# extension name and collect all files with same extension to a folder named
# like extension .

# For e.g. files with pdf extension all in one folder named pdf, files with jpg
# extension all in one folder named jpeg.


import os
import shutil
from os.path import isfile, join
mypath = '/home/kunal/Desktop'
os.chdir(mypath)
print(os.listdir('.'))
files = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
f = open('changes.txt', 'w')    # all changes done to your path are shown in this file inside txt folder.
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
        f.write("%s moved to %s\n" % (file, folder_name))
    except shutil.Error:
        raise shutil.Error("File already exists in the folder")
f.close()
print(os.listdir('.'))
