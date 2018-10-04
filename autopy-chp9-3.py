#! python3

import shutil, os
import re

datePattern = re.compile(r'.txt')    #search for .txt pattern

for amerFilename in os.listdir('.'):
    extension = os.path.splitext(amerFilename)[1]
    #print (extension)
    mo = datePattern.search(extension)
    if mo:
       # print (mo.group())
        print (amerFilename)
        shutil.copy(os.path.abspath(amerFilename), 'C:\\delicious')