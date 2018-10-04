#! python3

import shutil, os

for filename in os.listdir('.'):
    fileSize = os.path.getsize(filename)
    if fileSize > 100000000:
        print ('file' + filename + 'deleted')
       # os.unlink(filename)