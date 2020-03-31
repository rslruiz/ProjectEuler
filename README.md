# Project Euler

Problem 7: 10001st prime

```

def nthPrime(n):
    # Using Sieve of Erastosthenes
    MAX = 110000
    nums = [i for i in range(MAX)]
    isPrime = [True] * MAX

    p = 2
    while (p*p < MAX):
        if isPrime[p]:
            for i in range(p*p, MAX, p):
                isPrime[i] = False
        p += 1
    prime = [nums[i] for i in range(1,MAX) if isPrime[i]]
    return prime[n]

```

Problem 6: Sum square difference

Problem 5: Smallest multiple

Problem 4: Largest palindrome product

Problem 3: Largest prime factor

Problem 2: Even Fibonacci Numbers

Problem 1: Multiples of 3 and 5
