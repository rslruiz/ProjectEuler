"""Project Euler: Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the given number?

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

def largestPrimeFactor(n):

    for d in range(2, n):
#        print(f'{d}, ', end='')
        while n%d == 0:
            n //= d

        if d*d > n: break
#    print(n)
    return n


Test.assert_equals(largestPrimeFactor(2), 2)
Test.assert_equals(largestPrimeFactor(3), 3)
Test.assert_equals(largestPrimeFactor(5), 5)
Test.assert_equals(largestPrimeFactor(7), 7)
Test.assert_equals(largestPrimeFactor(13195), 29)
Test.assert_equals(largestPrimeFactor(600851475143), 6857)