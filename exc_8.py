def rps_comparison (p1,p2):
    if p1 == p2 :
        print("Its a tie!")
    elif p1 == "R" :
        if p2 == "P":
            print("player 2 Wins!")
        else :
            print("player 1 Wins!")
    elif p1 == "P" :
        if p2 == "R":
            print("player 1 Wins!")
        else :
            print("player 2 Wins!")
    elif p1 == "S" :
        if p2 == "R":
            print("player 1 Wins!")
        else :
            print("player 2 Wins!")
    print("player 1 : " + p1 + "\nplayer 2 : " + p2)

def start_rps_game():
    valid_inputs = ["R", "P", "S"]
    p1 = input("Player 1 Choose your weapon ( R, P, S ): ")
    p2 = input("Player 2 Choose your weapon ( R, P, S ): ")
    if p1 not in valid_inputs or p2 not in valid_inputs :
        print("Invalid input(s), try again.")
        start_rps_game()
    else :
        rps_comparison(p1,p2)
        if(input("Play again (y/n)?") == "y"):
            start_rps_game()

if __name__ == "__main__":
    start_rps_game()