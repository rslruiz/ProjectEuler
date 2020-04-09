"""Project Euler: Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
a +b +c = n
a^2 +b^2 = c^2; a = u - v; b = 2(uv)**0.5; c = u + v;
2(uv)**0.5 +2u = n; (uv)**0.5 = n/2 -u; v = 1/u(n/2 -u)**2; v = n*n/(4u) -n +u;

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

""" Euler9() Version 2, though this will not catch all triplets with the given sum.
"""
def specialPythagoreanTriplet(n):
    for u in range(2, n):
        if not (n*n)%(4*u):
            v = (n*n)//(4*u) -n +u
            if 0 < v and v < u:
                return 2*int((u*v)**0.5)*(u - v)*(u + v)

print(specialPythagoreanTriplet(36))
print(specialPythagoreanTriplet(1000))

Test.assert_equals(specialPythagoreanTriplet(24), 480)
Test.assert_equals(specialPythagoreanTriplet(36), 1620)
Test.assert_equals(specialPythagoreanTriplet(120), 49920) #, 55080, 60000
Test.assert_equals(specialPythagoreanTriplet(1000), 31875000)

