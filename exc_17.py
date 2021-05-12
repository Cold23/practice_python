import random

def guess_game_2() :
    number = "".join([str(random.choice(range(0,9))) for x in range(0,4)])
    guess = ""
    while number != guess and guess != "exit"  :
        print(number)
        guess = input("Guess my number (4 digts)? : ")
        cows = 0
        bulls = 0
        if guess == "exit":
            break
        for i in range(len(number)):
            if number[i] == guess[i]:
                cows = cows + 1
            elif guess[i] in number and guess[i] not in guess[:i] :
                bulls = bulls + 1
        if guess != number :
            print("Not Exacly.\nCows  : ",cows,"\nBulls : ",bulls)
        else :
            print("you guessed right!")

if __name__ == "__main__":
    guess_game_2()
    