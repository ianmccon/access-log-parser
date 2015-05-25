Parses lines from an apache access log and reports the following statistics

* Number of successfule requests per minute
* Number of error requests per minute
* Mean response time per minute
* MBs sent per minute


Usage:

    python parse_access_log.py <<logfile>>

This prints a report in the following format

    30/Mar/2015:11:11:
        Requests: 23 successful  0 error
        Mean response time: 543528 μs  MBs sent: 0.114 MB
