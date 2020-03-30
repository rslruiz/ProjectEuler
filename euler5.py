"""Project Euler: Problem 5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

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

from functools import reduce

def gcd(a, b):
    # Return greatest common divisor using Euclid's Algorithm.
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Return lowest common multiple.
    return a * b // gcd(a, b)

def smallestMult(n):
    return reduce(lcm,range(1,n+1))


Test.assert_equals(smallestMult(5), 60)
Test.assert_equals(smallestMult(7), 420)
Test.assert_equals(smallestMult(10), 2520)
Test.assert_equals(smallestMult(13), 360360)
Test.assert_equals(smallestMult(20), 232792560)
