#!/usr/bin/env python
# -*- coding: utf-8 -*-

# parse_access_log.py
#
# Author: Ian McConachie <ian@ianmcconachie.com>
# Date 25-05-2015
#
# This script takes an apache acces log file as input and generates the following metrics
#
# * Number of successful requests per minute
# * Number of error requests per minute
# * Mean response time per minute
# * MBs sent per minute
#
#
# Usage:
#
#     python parse_access_log.py <<logfile>>
#
# This prints a report in the following format
#
#     30/Mar/2015:05:04: Requests: 816 successful  2 error - Mean response time: 350734μs - MBs sent: 13.938MB
#

import sys

totals = {}

def parse_line(line):
    '''
    Function that parses each line of the log and extracts the required data
    and stores this in a dictionary
    '''
    data = line.split()
    time = data[3][1:-3]
    status = data[8]
    data_sent = data[9]
    response_time = int(data[10])

    if time not in totals:
        totals[time] = {
            'count': 0,
            'success': 0,
            'error': 0,
            'response_time': 0,
            'bytes_sent': 0
            }

    if data_sent == '-':
        bytes_sent = 0
    else:
        bytes_sent = int(data_sent)

    if status[0] == '2':
        totals[time]['success'] += 1
    else:
        totals[time]['error'] += 1

    totals[time]['count'] += 1
    totals[time]['response_time'] += response_time
    totals[time]['bytes_sent'] += bytes_sent


def print_results(totals):
    '''
    Function to print the data gleaned from the access log
    in a easily readable format
    '''
    for key in sorted(totals):
        mean_response_time = totals[key]['response_time'] / totals[key]['count']
        mb_sent = totals[key]['bytes_sent'] / (1024.0*1024.0)
        print '%s: Requests: %s successful  %s error - Mean response time: %sμs - MBs sent: %0.3fMB' % (key, totals[key]['success'], totals[key]['error'], mean_response_time, mb_sent)


# Main routine
def main(filename):
    # Open log file from disk
    try:
        log = open(filename, 'r')
    except IOError:
        print 'The log file specified could not be found'
        return

    for line in log.readlines():
        parse_line(line)

    print_results(totals)


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
        main(filename)
    else:
        print 'You must specify the log filename'
        print 'Usage: python parse_access_log.py <<logfile>>'

