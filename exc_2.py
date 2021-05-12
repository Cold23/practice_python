if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if number % 4 == 0 :
        print("the number you entered is a multiple of 4")
    elif number % 2 == 0 :
        print("the number you entered is a even")
    else:
        print("the number you entered is odd")
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter another number: "))
    if number_1 % number_2 == 0:
        print(str(number_1)+" divides "+str(number_2))
    else:
        print(str(number_1)+" does not divide "+str(number_2))