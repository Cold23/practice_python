import math

def triangular_divisior():
    curr = 0
    limit = 500
    max_tri = limit * 2
    divisors = []
    curr = sum(range(max_tri+1))
    while len(divisors) < limit :
        max_tri += 1
        divisors.clear()
        for i in range(1,math.floor(curr**0.5) + 1):
            if curr % i == 0 :
                divisors.append(i)
        curr += max_tri
    return curr

if __name__ == "__main__":
    print(triangular_divisior())