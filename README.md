# Project Euler
Problem 10: Summation of primes
```Python
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

```

Problem 9: Special Pythagorean triplet
```Python
# Euler9() Version 2, though this will not catch all triplets with the given sum.

def specialPythagoreanTriplet(n):
    for u in range(2, n):
        if not (n*n)%(4*u):
            v = (n*n)//(4*u) -n +u
            if 0 < v and v < u:
                return 2*int((u*v)**0.5)*(u - v)*(u + v)

print(specialPythagoreanTriplet(36))
print(specialPythagoreanTriplet(1000))

```

Problem 8: Largest product in a series

Problem 7: 10001st prime

Problem 6: Sum square difference

Problem 5: Smallest multiple

Problem 4: Largest palindrome product

Problem 3: Largest prime factor

Problem 2: Even Fibonacci Numbers

Problem 1: Multiples of 3 and 5
