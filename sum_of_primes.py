def prime(i, primes):
    for prime in primes:
        if not i % prime:
            return False
    primes.add(i)
    return i

def find_primes(n):
    primes = set([2])
    i = 2
    while True:
        if prime(i, primes):
            if len(primes) == n:
                return primes
        i += 1

if __name__ == "__main__":
    print(sorted(find_primes(10)))