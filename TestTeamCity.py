#print "Test TeamCity"
import unittest
from NumFilter import NumFilter 

"""
class NumFilter(Object):
    def filter(self, number):
        "filter num"
        if number > 10:
            return 1
        elif number > 10 and number < 20:
            return 2
        else:
            return 0
"""

class TestFiler(unittest.TestCase):
    def test_bigger(self):
        filter_1 = NumFilter()
        self.assertEqual(filter_1.filter(12), 1)

