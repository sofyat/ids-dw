#!/usr/bin/env python2

"""BatchReader.py: reads the batch file"""

import getopt
import os # for linesep
from pprint import pprint
import string
import sys

from Payments import Payments

"""
BatchReader: reads the batch file and updates payment info
"""
class BatchReader :
    def __init__(self, payments):
        self._payments = payments

    def read(self, infname):
        f = open(infname, 'r')
        header = f.readline()
        for line in f:
            lst = [l.strip(' ') for l in line.rstrip(os.linesep).split(', ')]
            if(len(lst) < 4):
                continue
            try:
                id1 = int(lst[1])
                id2 = int(lst[2])
            except Exception:
                print("Error parsing line: ", line)
                continue
            self._payments.add(id1, id2)
        f.close()





