#!/usr/bin/env python

from glob import glob
from os import chdir, sep as SEP
from os.path import abspath, dirname, join
from time import localtime
from zipfile import ZipFile, ZIP_DEFLATED

NAME = 'RobotDemo'
ZIP_NAME = NAME + '-%d%02d%02d.zip' % localtime()[:3]
FILES = ['README.rst',
         'calculator.py',
         'CalculatorLibrary.py',
         'keyword_driven.txt',
         'data_driven.txt',
         'gherkin.txt']

chdir(dirname(abspath(__file__)))
zipfile = ZipFile(ZIP_NAME, 'w', ZIP_DEFLATED)
for pattern in FILES:
    for path in glob(pattern.replace('/', SEP)):
        print 'Adding:  ', path
        zipfile.write(path, join(NAME, path))
zipfile.close()
print 'Created: ', ZIP_NAME
