Parses lines from an apache access log and reports the following statistics

* Number of successful requests per minute
* Number of error requests per minute
* Mean response time per minute
* MBs sent per minute


Usage:

    python parse_access_log.py <<logfile>>

This prints a report in the following format

    30/Mar/2015:05:04: Requests: 816 successful  2 error - Mean response time: 350734μs - MBs sent: 13.938MB
