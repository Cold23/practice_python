import string
import random

if __name__ == "__main__":
    strength = int(input("How strong? (1 = weak , 2 = strong) : "))
    chars = string.ascii_letters
    alphas = string.digits
    min_char = 6
    max_char = 10
    if strength == 2:
        test = [random.choice(chars) + random.choice(alphas) for x in range(random.randint(min_char, max_char))]
        random.shuffle(test)
        password = "".join(test)
    else :
        password = "".join(random.choice(chars) for x in range(0,min_char))
    print ("This is your password : ",password)

