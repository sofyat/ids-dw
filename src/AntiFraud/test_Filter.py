#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys
import unittest

# tests for Filter.py
from Filter import Filter


class TestFilterMethods(unittest.TestCase):

    def test_init(self):
        filter = Filter()
        self.assertFalse(filter == None)

    def test_key(self):
        id1 = "foo"
        id2 = "bar"
        filter = Filter()
        key = filter._key(id1, id2)
        self.assertEqual(key, 'foo,bar')
        
    def test_add(self):
        filter = Filter()
        self.assertFalse(filter.add('a', 'b'))
        self.assertTrue(filter.add('a', 'b'))

    def test_contains(self):
        filter = Filter()
        self.assertFalse(filter.add('a', 'b'))
        self.assertTrue(filter.add('a', 'b'))
        self.assertFalse(filter.contains('a', 'c'))
        self.assertTrue(filter.contains('a', 'b'))
        self.assertTrue(filter.contains('b', 'a'))

if __name__ == '__main__':
    unittest.main()
