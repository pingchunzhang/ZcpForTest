#print "Test TeamCity"
#import unittest

class NumFilter(Object)

    def filter(self, number):
        """filter num"""
        if number < 10:
            return 1
        elif number > 10 and number < 20:
            return 2
        else:
            return 0
        
    def compare(self, number1, number2):
        """compare number"""
        if number1 > number2:
            return "bigger"
        elif number1 == number2:
            return "equal"
        else:
            return "smaller"

