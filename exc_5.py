import random

if __name__ == "__main__":
  a = random.sample(range(1000),random.randint(50,100))
  b = random.sample(range(1000),random.randint(50,100))
  print([i for i in a if i in b])