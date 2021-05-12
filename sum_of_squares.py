if __name__ == "__main__":
    res  = - sum([x**2 for x in range(1,101)]) + sum([x for x in range(1,101)])**2
    print(res)