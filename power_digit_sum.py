def digit_sum(n):
    n = str(n)
    x = sum([int(i) for i in n])
    return x

if __name__ == "__main__":
    print(digit_sum(2**1000))