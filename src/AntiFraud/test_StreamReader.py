#!/usr/bin/env python2

import getopt
import os # for linesep
from pprint import pprint
import string
import sys
import unittest
import filecmp
import tempfile
from subprocess import call

# tests StreamReader
from Payments import Payments
from StreamReader import StreamReader


class TestStreamReaderMethods(unittest.TestCase):

    def test_init(self):
        payments = Payments()
        degrees = [1,2,4]
        first_output_file = './test-outputs/out1.txt'
        second_output_file = './test-outputs/out2.txt'
        third_output_file = './test-outputs/out3.txt'
       
        outfiles = [ first_output_file, second_output_file, third_output_file ]
        for fname in outfiles:
            if not os.path.exists(os.path.dirname(fname)):
                try:
                    os.makedirs(os.path.dirname(fname))
                except OSError as exc: 
                    if exc.errno != errno.EEXIST:
                        raise
        streamreader = StreamReader(payments, degrees, outfiles)
        self.assertFalse(streamreader == None)
        
    def _create_output_files(self):
        first_output_file = './test-outputs/out1.txt'
        second_output_file = './test-outputs/out2.txt'
        third_output_file = './test-outputs/out3.txt'
        outfiles = [ first_output_file, second_output_file, third_output_file ]
        for fname in outfiles:
            if not os.path.exists(os.path.dirname(fname)):
                try:
                    os.makedirs(os.path.dirname(fname))
                except OSError as exc: 
                    if exc.errno != errno.EEXIST:
                        raise
        return outfiles

    def _create_payments_obj(self):
        payments = Payments()
        payments.add(11, 12)
        payments.add(12, 13)
        payments.add(13, 14)
        payments.add(14, 15)
        payments.add(15, 16)
        return payments

    def test_process(self):
        degrees = [1,2,4]
        outfiles = self._create_output_files()
        payments = self._create_payments_obj()
        streamreader = StreamReader(payments, degrees, outfiles)
        streamreader.process(11, 12)
        streamreader.process(11, 13)
        streamreader.process(11, 14)
        streamreader.process(11, 16)
        streamreader._close_output_files()
        opath = tempfile.mkstemp()[1]
        with open(opath, 'w') as f:
            f.write("trusted\nunverified\nunverified\nunverified\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[0], opath))
        with open(opath, 'w') as f:
            f.write("trusted\ntrusted\ntrusted\nunverified\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[1], opath))
        with open(opath, 'w') as f:
            f.write("trusted\ntrusted\ntrusted\ntrusted\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[2], opath))

    def test_process_repeats(self):
        degrees = [1,2,4]
        outfiles = self._create_output_files()
        payments = Payments()
        streamreader = StreamReader(payments, degrees, outfiles)
        streamreader.process(11, 12)
        streamreader.process(11, 12)
        streamreader._close_output_files()
        opath = tempfile.mkstemp()[1]
        with open(opath, 'w') as f:
            f.write("unverified\ntrusted\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[0], opath))
        self.assertTrue(filecmp.cmp(outfiles[1], opath))
        self.assertTrue(filecmp.cmp(outfiles[2], opath))

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
            f.write("2016-11-02 09:38:53, 11, 15, 3.19, myline1\n")
            f.close()
        degrees = [1,2,4]
        outfiles = self._create_output_files()
        payments = self._create_payments_obj()
        streamreader = StreamReader(payments, degrees, outfiles)
        streamreader.read(fname)
        streamreader._close_output_files()
        opath = tempfile.mkstemp()[1]
        with open(opath, 'w') as f:
            f.write("trusted\nunverified\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[0], opath))
        with open(opath, 'w') as f:
            f.write("trusted\nunverified\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[1], opath))
        with open(opath, 'w') as f:
            f.write("trusted\ntrusted\n")
            f.close()
        self.assertTrue(filecmp.cmp(outfiles[2], opath))


if __name__ == '__main__':
    unittest.main()
