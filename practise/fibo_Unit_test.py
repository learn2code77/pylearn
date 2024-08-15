''' Unit testing'''

import unittest
import Lists.fibonacci as fib

class TestFibo(unittest.TestCase):
    ''' A test class'''

    def fibo_test(self):
        ''' A test function '''
        fibo_series = [0,1,1,2,3,5]
        result = fib.fibFind(5)
        self.assertEqual(fibo_series, result)

if __name__ == "__main__":
    unittest.main()
