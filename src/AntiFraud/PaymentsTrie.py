#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys

# https://github.com/google/pygtrie: 
# pip install pygtrie
# http://pygtrie.readthedocs.io/en/stable/
import pygtrie as trie

"""
Trie-based implementation of Payments to use instead of the default, 
dictionary based approach.
Is more memory efficient since the id's of the payments have
overlapping prefixes and therefore we expect this to use the same 
amount of space as the dictionary-based implemention.
"""
class PaymentsTrie :
    def __init__(self):
        self._trie = trie.CharTrie()

    def _key(self, id1, id2):
        return str(id1) + "," + str(id2)

    def add(self, id1, id2):
        key1 = self._key(id1, id2)
        key2 = self._key(id2, id1)
        self._trie[key1] = True
        self._trie[key2] = True

    def contains(self, id1, id2):
        key1 = self._key(id1, id2)
        key2 = self._key(id2, id1)
        return (key1 in self._trie) or (key2 in self._trie)
        
    def connected(self, id1, id2, degree):
        if(id1 == id2):
            return True
        if(degree == 0):
            return False
        if(self.contains(id1,id2) == True):
            return True
        id1_s = str(id1) + ","
        id2_s = str(id2) + ","
        if((not self._trie.has_subtrie(id1_s)) or 
           (not self._trie.has_subtrie(id2_s))):
            return False
        try: 
            for(k, v) in self._trie.iteritems(id1_s):
                if(k == None or v == None):
                    continue
                (id1_k, id2_k) = str.split(k, ',')
                if(self.connected(id2_k, id2, degree -1) == True):
                    return True
        except KeyError:
            print("Error with prefix ", id1_t)
        return False
        
            
    def dump(self):
        print("dump: ")
        pprint(self._trie)
        print("---")

        
        



