if __name__ == "__main__":
    num = int(input("Enter a number: "))
    x = range(1, num+1)
    print([i for i in x if num % i == 0])
