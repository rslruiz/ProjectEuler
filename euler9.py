"""Project Euler: Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
a +b +c = n
a^2 +b^2 = c^2; a = 2uv; b = u^2 - v^2; c = u^2 + v^2;
2uv +2u^2 = n; 2u(v+u) = n; v = n/2u - u;

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

def specialPythagoreanTriplet(n):
    for u in range(2, int(n**0.5)):
        if not n%(2*u):
            v = n//(2*u) -u
            if v > u or v <=0:
                continue
            return (2*u*v)*(u*u - v*v)*(u*u + v*v)


Test.assert_equals(specialPythagoreanTriplet(24), 480)
Test.assert_equals(specialPythagoreanTriplet(120), 49920) #, 55080, 60000
Test.assert_equals(specialPythagoreanTriplet(1000), 31875000)

