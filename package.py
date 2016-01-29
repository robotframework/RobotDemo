#!/usr/bin/env python

from __future__ import print_function

from os import getcwd
from os.path import abspath, dirname, join
from time import localtime
from zipfile import ZipFile, ZIP_DEFLATED

assert getcwd() == dirname(abspath(__file__))

NAME = 'RobotDemo'
ZIP_NAME = NAME + '-%d%02d%02d.zip' % localtime()[:3]
FILES = ['README.rst',
         'calculator.py',
         'CalculatorLibrary.py',
         'keyword_driven.robot',
         'data_driven.robot',
         'gherkin.robot']

with ZipFile(ZIP_NAME, 'w', ZIP_DEFLATED) as zipfile:
    for path in FILES:
        print('Adding:  ', path)
        zipfile.write(path, join(NAME, path))

print('Created: ', ZIP_NAME)
