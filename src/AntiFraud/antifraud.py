#!/usr/bin/env python2


"""
antifraud.py: https://github.com/InsightDataScience/digital-wallet
Implementation of simple antifraud filter using dictionary.
"""
__author__ = "S Irwin"
__version__ = "0.0.1"


import getopt
import os # for linesep
from pprint import pprint
import string
import sys

from Payments import Payments
from BatchReader import BatchReader
from StreamReader import StreamReader

def usage():
    print("Usage: " + sys.argv[0]  
          + " <path-to-batch-payment.txt>"  
          + " <path-to-stream-payment.txt>" 
          + " <path-to-output1.txt>"  
          + " <path-to-output2.txt>"  
          + " <path-to-output3.txt>")


def main():

    batch_payment_file = ''
    stream_payment_file = ''
    first_output_file = ''
    second_output_file = ''
    third_output_file = ''
    if(len(sys.argv) == 6):
        batch_payment_file   = sys.argv[1]
        stream_payment_file  = sys.argv[2]
        first_output_file    = sys.argv[3]
        second_output_file   = sys.argv[4]
        third_output_file    = sys.argv[5]
    else:
        usage()
        exit(0)
        
    print "batch_payment_file: "  + batch_payment_file
    print "stream_payment_file: " + stream_payment_file
    print "first_output_file: "   + first_output_file
    print "second_output_file: "  + second_output_file
    print "third_output_file: "  + third_output_file

    payments = Payments()
    batchreader = BatchReader(payments)
    batchreader.read(batch_payment_file)
    degrees = [1,2,4]
    outfiles = [ first_output_file, second_output_file, third_output_file ]
    streamreader = StreamReader(payments, degrees, outfiles)
    streamreader.read(stream_payment_file)



if __name__ == '__main__':
    main()
