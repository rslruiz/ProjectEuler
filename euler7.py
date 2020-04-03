"""Project Euler: Problem 7: 10001st prime

RSLRuiz March 2020
"""

class Test(object):
    @classmethod
    def assert_equals(self,actual,expected, text=''):
#        print(actual, expected)
        if actual == expected:
            return print(f'pass')
        else:
            return print(f'fail {text}')

def nthPrime(n):
    # Using Sieve of Erastosthenes
    MAX = 110000
    # nums = [i for i in range(MAX)]
    isPrime = [True] * MAX

    p = 2
    while (p*p < MAX):
        if isPrime[p]:
            for i in range(p*p, MAX, p):
                isPrime[i] = False
        p += 1
    # prime = [nums[i] for i in range(1,MAX) if isPrime[i]]
    prime = [i for i in range(1,MAX) if isPrime[i]]
    return prime[n]


Test.assert_equals(nthPrime(6), 13)
Test.assert_equals(nthPrime(10), 29)
Test.assert_equals(nthPrime(100), 541)
Test.assert_equals(nthPrime(1000), 7919)
Test.assert_equals(nthPrime(10001), 104743)
