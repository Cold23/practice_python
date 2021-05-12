def checkPrimality():
    x = int(input("Enter a number (CTRL + C to exit):\n"))
    for i in range(2,round(x/2)+2):
        if x % i == 0 :
            print(str(x) + " is not a prime number.")
            break
        if i == round(x/2)+1:
            print(str(x) + " is a prime number!")
            break

if __name__ == "__main__":

    while True :
        checkPrimality()
    