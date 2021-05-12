if __name__ == "__main__":
    data = [x for x in range(1001) if x % 3 == 0 or x % 5 == 0]
    print(sum(data))