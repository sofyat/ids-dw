#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys

# https://github.com/jaybaird/python-bloomfilter
from pybloom import ScalableBloomFilter 

"""
Filter: A class which wraps a bloom filter which can speed up whether we have
previously seen a particular id
Since we have no way to obtain the list of id's which a particular party
has already Paid to, we cannot use this other than for a Feature 1 
implementation.
"""
class Filter :
    def __init__(self):
        self._sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)

    def _key(self, id1, id2):
        return str(id1) + "," + str(id2)

    def add(self, id1, id2):
        return self._sbf.add(self._key(id1, id2))

    def contains(self, id1, id2):
        if(self._key(id1, id2) in self._sbf):
            return True
        if(self._key(id2, id1) in self._sbf):
            return True
        return False

