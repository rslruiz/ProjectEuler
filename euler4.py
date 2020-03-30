"""Project Euler: Problem 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.

RSLRuiz
"""

class Test(object):
    @classmethod
    def assert_equals(self,actual,expected, text=''):
        if actual == expected:
            return print(f'pass')
        else:
            return print(f'fail {text}')

def largestPalindromeProduct(n):
    max = int('9'*n)
    min = 9*10**(n-1)
    for i in range(max, min,-1):
        for j in range(i, min,-1):
            prod = i*j
            if ispalindrome(prod):
                return prod # , i, j
    return -1

def ispalindrome(n):
    pal = palin = n; drome = 0
    while pal != 0:
        drome = drome*10 + pal%10
        pal//=10
    if palin - drome == 0:
        return True
    else: return False

print(largestPalindromeProduct(2))
print(largestPalindromeProduct(3))
print(largestPalindromeProduct(4))
print(largestPalindromeProduct(5))
print(largestPalindromeProduct(6))


Test.assert_equals(largestPalindromeProduct(2), 9009)
Test.assert_equals(largestPalindromeProduct(3), 906609)
