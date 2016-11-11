#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys
import unittest

# tests Payments.py 
from Payments import Payments

class TestPaymentsMethods(unittest.TestCase):

    def test_init(self):
        payments = Payments()
        self.assertFalse(payments == None)
        
    def test_add(self):
        payments = Payments()
        payments.add('111', '222')

    def test_contains(self):
        payments = Payments()
        payments.add('111', '222')
        self.assertTrue(payments.contains('111', '222'))
        self.assertTrue(payments.contains('222', '111'))
        self.assertFalse(payments.contains('111', '333'))

    def test_connected(self):
        payments = Payments()
        payments.add('111', '222')
        self.assertTrue(payments.connected('111', '111', 0))
        self.assertTrue(payments.connected('111', '222', 1))
        self.assertTrue(payments.connected('111', '222', 2))
        self.assertTrue(payments.connected('222', '111', 1))
        self.assertFalse(payments.connected('222', '111', 0))
        payments.add('222', '333')
        payments.add('333', '444')
        payments.add('444', '555')
        self.assertTrue(payments.connected('111', '333', 2))
        self.assertTrue(payments.connected('111', '444', 3))
        self.assertTrue(payments.connected('111', '555', 4))
        self.assertTrue(payments.connected('111', '555', 4))

if __name__ == '__main__':
    unittest.main()
