from apache_log_parser import make_parser
from pprint import pprint

line_parser = make_parser('%a %l %u %t \"%r\" %>s %b %D')

totals = {}

successful_requests = 0
error_requests = 0

def log_data(line_data):
    '''
    Function to pull values from parsed log line
    and saved cumulative values to totals dictionary
    '''
    response_time = int(line_data['time_us'])
    if line_data['response_bytes_clf'] == '-':
        mb_sent = 0
    else:
        mb_sent = int(line_data['response_bytes_clf'])

    if line_data['status'][0] == '2':
        totals[time]['success'] += 1
    else:
        totals[time]['error'] += 1

    totals[time]['count'] += 1
    totals[time]['response_time'] += response_time
    totals[time]['mb_sent'] += mb_sent

def print_results(totals):
    '''
    Function to print the data gleaned from the access log
    in a easily readable format
    '''
    for key in sorted(totals):
        mean_response_time = totals[key]['response_time'] / totals[key]['count']

        print '%s:' % key
        print '    Requests: %s successful  %s error' % (totals[key]['success'], totals[key]['error'])
        print '    Mean response time: %s  MBs sent: %s' % (mean_response_time, totals[key]['mb_sent'])



log = open('web-access.log', 'r')

for line in log.readlines():
    line_data = line_parser(line)
    time = line_data['time_received_datetimeobj'].strftime("%d-%m-%Y %H:%M")

    if time not in totals:
        totals[time] = {
            'count': 0,
            'success': 0,
            'error': 0,
            'response_time': 0,
            'mb_sent': 0
            }
    log_data(line_data)


print_results(totals)



