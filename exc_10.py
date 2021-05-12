import numpy as np

if __name__ == "__main__":
    a = np.random.choice(100,50,replace = True)
    b = np.random.choice(100,50,replace = True)
    print(sorted(list(dict.fromkeys([x for x in a if x in b]))))