"""Project Euler: Problem 10: Summation of primes

Find the sum of all the primes below n.

RSLRuiz April 2020
"""

class Test(object):
    @classmethod
    def assert_equals(self,actual,expected, text=''):
#        print(actual, expected)
        if actual == expected:
            return print(f'pass')
        else:
            return print(f'fail {text}')

def primeSummation(n):
    # Using Sieve of Erastosthenes
    isPrime = [True] * n
    p = 2
    while (p * p < n):
        if isPrime[p]:
            for i in range(p * p, n, p):
                isPrime[i] = False
        p += 1

    return sum([i for i in range(2, n) if isPrime[i]])


print(primeSummation(2000000))

Test.assert_equals(primeSummation(17), 41)
Test.assert_equals(primeSummation(2001), 277050)
Test.assert_equals(primeSummation(140759), 873608362)
Test.assert_equals(primeSummation(2000000), 142913828922)

