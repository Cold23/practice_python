import math


def find_prime_factors(x):
    factors = [i for i in range(2, x) if x % i == 0]
    seq = []
    for y in factors:
        temp = math.floor(y**0.5)
        if len([k for k in range(temp, y) if y % k == 0 and k != 1]) == 0:
            seq.append(y)
    return seq


if __name__ == "__main__":
    print(find_prime_factors(int(input('Enter number'))))
