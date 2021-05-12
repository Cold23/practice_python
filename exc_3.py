if __name__ == "__main__":
    oper = int(input("Enter a number: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,10,20,30,50,25,21]
    print([num for num in a if num < oper])