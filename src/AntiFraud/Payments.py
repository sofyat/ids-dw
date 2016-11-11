#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys

"""
Dictionary (hash table) -based implementation of Payments.
Provided as default since it uses native python libs.
See also PaymentsTrie.py for a Trie based implementation.
"""
class Payments :
    def __init__(self):
        self._dict = {}
       
    def add(self, id1, id2):
        if(self._dict.has_key(id1) == False):
            self._dict[id1] = {}
        self._dict[id1][id2] = 1
        if(self._dict.has_key(id2) == False):
            self._dict[id2] = {}
        self._dict[id2][id1] = 1

    def contains(self, id1, id2):
        if(self._dict.has_key(id1) == 0):
            return False
        return  self._dict[id1].has_key(id2)

    def connected(self, id1, id2, degree):
        if(id1 == id2):
            return True
        if((not self._dict.has_key(id1)) or (not self._dict.has_key(id2))):
            return False
        if(degree == 0):
            return False
        if(self.contains(id1, id2)  == True):
            return True
        if(degree == 1):
            return False
        for k in self._dict[id1]:
            if(self.connected(k, id2, degree - 1) == True):
                return True
        return False

    def dump(self):
        print("dump: ")
        pprint(self._dict)
        print("---")

