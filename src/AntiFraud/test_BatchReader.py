#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys
import unittest

# tests BatchReader
from Payments import Payments
from BatchReader import BatchReader

class TestBatchReaderMethods(unittest.TestCase):

    def test_init(self):
        payments = Payments()
        batchreader = BatchReader(payments)
        self.assertFalse(batchreader == None)
        
    def test_read(self):
        fname = './test-inputs/batch_payments.short.csv'
        if not os.path.exists(os.path.dirname(fname)):
            try:
                os.makedirs(os.path.dirname(fname))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(fname, "w") as f:
            f.write("time, id1x, id2x, amount, message\n")
            f.write("2016-11-02 09:38:53, 11, 12, 3.19, myline1\n")
            f.write("2016-11-02 09:38:54, 12, 13, 3.20, myline2\n")
            f.write("2016-11-02 09:38:55, 13, 14, 3.21, myline3\n")
        f.close()
        payments = Payments()
        batchreader = BatchReader(payments)
        batchreader.read(fname)
        self.assertTrue(payments.connected(11,14,3))

if __name__ == '__main__':
    unittest.main()
