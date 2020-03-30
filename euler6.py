"""Project Euler: Problem 5: Sum square difference
    Find the difference between the sum of the squares
    of the first n natural numbers and the square of the sum.

RSLRuiz
"""

class Test(object):
    @classmethod
    def assert_equals(self,actual,expected, text=''):
#        print(actual, expected)
        if actual == expected:
            return print(f'pass')
        else:
            return print(f'fail {text}')

def sumSquareDifference(n):
    return sum(i for i in range(n+1))**2 - sum( i**2 for i in range(n+1))


Test.assert_equals(sumSquareDifference(10), 2640)
Test.assert_equals(sumSquareDifference(20), 41230)
Test.assert_equals(sumSquareDifference(100), 25164150)
