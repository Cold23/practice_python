import math

def guess_game_2():
    guesses = 0
    l = 0
    r = 100
    pinput = ""
    while pinput != "yes" and l <= r:
        curr = math.floor((l + r)/2)
        text = "Are you thinking of "+str(curr)+"?(bigger,smaller)"
        pinput = input(text)
        guesses += 1
        if pinput == "bigger":
            l = curr
        elif pinput == "smaller":
            r = curr
        elif pinput == "yes":
           print("I won after "+ str(guesses))
        elif pinput == "exit":
            break
    pinput = input("Play again?(Y/N): ")
    if pinput == "y":
        guess_game_2()
            


if __name__ == "__main__":
    guess_game_2()
