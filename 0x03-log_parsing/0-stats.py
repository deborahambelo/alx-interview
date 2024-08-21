#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""
import sys

def parseLogs():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    stdin = sys.stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            try:
                ip, timestamp, method, path, protocol, status, size = line.strip().split()
            except ValueError:
                continue
            try:
                fileSize += int(size)
                if status in codes:
                    statusCodes[status] = statusCodes.get(status, 0) + 1
            except ValueError:
                pass
            if lineNumber % 10 == 0:
                report(fileSize, statusCodes)
    except KeyboardInterrupt:
        report(fileSize, statusCodes)
        raise

def report(fileSize, statusCodes):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): total log size after every 10 successfully read line
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for code in sorted(codes):
        if code in statusCodes:
            print("{}: {}".format(code, statusCodes[code]))

if __name__ == '__main__':
    parseLogs()
