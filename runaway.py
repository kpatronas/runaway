#!/usr/bin/env python3
import sys
import base64
import argparse
from datetime import datetime

def stdin2b64():
    '''
    Read stin and store results
    '''
    input_lines = ""
    for line in sys.stdin:
        input_lines += line
    input_lines = input_lines.encode('utf-8')
    b64 = base64.b64encode(input_lines)
    return b64

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create a log file with a timestamp,label and standard input')
    parser.add_argument('-l','--label', help='Label',required = True)
    args = parser.parse_args()
    stdin_b64 = stdin2b64()
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print('%s,%s,%s'%(ts,args.label,stdin_b64.decode('utf-8')))
