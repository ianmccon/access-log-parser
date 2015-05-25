import unittest
import parse_access_log

class AccessLogParserTestCase(unittest.TestCase):

    def test_a(self):
        '''
        Test case with log line with all data and successful reponse
        '''
        data = None
        test_line = '127.0.0.1 - - [30/Mar/2015:05:04:20 +0100] "GET /render/?from=-11minutes&until=-5mins&uniq=1427688307512&format=json&target=alias%28movingAverage%28divideSeries%28sum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalMillis.count%29%29%2Csum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalCalls.count%29%29%29%2C%275minutes%27%29%2C%22Latency%22%29 HTTP/1.1" 200 157 165169'
        data = parse_access_log.parse_line(test_line)

        self.assertNotEqual(data, None)
        self.assertEqual(data[0], '30/Mar/2015:05:04')
        self.assertEqual(data[1], 1)
        self.assertEqual(data[2], 0)
        self.assertEqual(data[3], 165169)
        self.assertEqual(data[4], 157)

    def test_b(self):
        '''
        Test case with log line with no response data sent and successful reponse
        '''
        data = None
        test_line = '127.0.0.1 - - [30/Mar/2015:05:04:20 +0100] "GET /render/?from=-11minutes&until=-5mins&uniq=1427688307512&format=json&target=alias%28movingAverage%28divideSeries%28sum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalMillis.count%29%29%2Csum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalCalls.count%29%29%29%2C%275minutes%27%29%2C%22Latency%22%29 HTTP/1.1" 200 - 165169'
        data = parse_access_log.parse_line(test_line)
        self.assertNotEqual(data, None)
        self.assertEqual(data[0], '30/Mar/2015:05:04')
        self.assertEqual(data[1], 2)
        self.assertEqual(data[2], 0)
        self.assertEqual(data[3], 330338)
        self.assertEqual(data[4], 157)

    def test_c(self):
        '''
        Test case with log line with no data sent and error reponse
        '''
        data = None
        test_line = '127.0.0.1 - - [30/Mar/2015:05:04:20 +0100] "GET /render/?from=-11minutes&until=-5mins&uniq=1427688307512&format=json&target=alias%28movingAverage%28divideSeries%28sum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalMillis.count%29%29%2Csum%28nonNegativeDerivative%28collector.uk1.rou.*rou*.svc.*.RoutesService.routedate.total.processingLatency.totalCalls.count%29%29%29%2C%275minutes%27%29%2C%22Latency%22%29 HTTP/1.1" 401 - 165169'
        data = parse_access_log.parse_line(test_line)
        self.assertNotEqual(data, None)
        self.assertEqual(data[0], '30/Mar/2015:05:04')
        self.assertEqual(data[1], 2)
        self.assertEqual(data[2], 1)
        self.assertEqual(data[3], 495507)
        self.assertEqual(data[4], 157)

if __name__ == '__main__':
    unittest.main()
