#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys
import unittest

from PaymentsTrie import PaymentsTrie


class TestPaymentsTrieMethods(unittest.TestCase):

    def test_init(self):
        payments = PaymentsTrie()
        self.assertFalse(payments == None)

    def test_key(self):
        payments = PaymentsTrie()
        key = payments._key(11, 12)
        self.assertTrue(key == "11,12")
        
    def test_add(self):
        payments = PaymentsTrie()
        payments.add(11, 12)

    def test_contains(self):
        payments = PaymentsTrie()
        payments.add(11, 12)
        self.assertTrue(payments.contains(11,12))

    def test_connected(self):
        payments = PaymentsTrie()
        payments.add(11, 12)
        payments.add(11, 10)
        payments.add(12, 13)
        payments.add(13, 14)
        payments.add(14, 15)
        #payments.dump()
        self.assertTrue(payments.connected(11,11,0))
        self.assertTrue(payments.connected(11,12,1))
        self.assertTrue(payments.connected(12,13,1))
        self.assertTrue(payments.connected(11,15,4))
        self.assertFalse(payments.connected(11,15,3))
        self.assertTrue(payments.connected(10,11,1))


if __name__ == '__main__':
    unittest.main()
