#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys

from Payments import Payments

"""
StreamReader: a class to implement the reading a processing of a stream
"""
class StreamReader :
    def __init__(self, payments, degrees, outfiles):
        self._payments = payments
        self._degrees = degrees
        self._outfilenames = outfiles
        self._open_output_files()

    def __del__(self):
        self._close_output_files()

    def _open_output_files(self):
        if(len(self._degrees) != len(self._outfilenames)):
            raise RuntimeError('the number of outfiles names should be same as number of degrees')
        self._outputfiles = []
        for fname in self._outfilenames:
            f = open(fname, 'w')
            self._outputfiles.append(f)

    def _close_output_files(self):
        for f in self._outputfiles:
            f.close()

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
            self.process(id1, id2)
        f.close()
        self._close_output_files()

    def process(self, id1, id2):
        # first, write output lines
        for i, degree in enumerate(self._degrees):
            if i > len(self._outputfiles):
                raise RuntimeError('not enough outputfiles')
            f = self._outputfiles[i]
            if self._payments.connected(id1, id2, degree) :
                f.write("trusted\n")
            else :
                f.write("unverified\n")
        # second, add in the new payment information
        self._payments.add(id1, id2) # assume all new payments valid




