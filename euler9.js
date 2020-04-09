/* Project Euler: Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
a +b +c = n
a^2 +b^2 = c^2; a = u - v; b = 2uv; c = u + v;
2(uv)**0.5 +2u = n; (uv)**0.5 = n/2 -u; v = 1/u(n/2 -u)**2; v = n*n/(4u) -n +u;

Version 2, though this will not catch all triplets with the given sum.

RSLRuiz April 2020
*/

function specialPythagoreanTriplet(n) {
    for (let u = 2; u < n; u++) {
        if ((n*n)%(4*u) == 0) {
            let v = (n*n)/(4*u) -n +u;
            if (v > 0 && v < u)
                return 2*((u*v)**0.5)*(u - v)*(u + v);
        }
    }
}

console.log(specialPythagoreanTriplet(36))
console.log(specialPythagoreanTriplet(1000))
