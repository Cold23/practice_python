import random

if __name__ == "__main__":
    a = random.sample(range(1000),random.randint(50,100))
    print([x for x in a if x % 2 == 0])