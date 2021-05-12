import random

def print_word_board(guessed_word):
    for x in guessed_word:
        print(x+" ", end="")
    print("")

def pick_a_word():
    with open("sowpods.txt",'r') as open_file:
        all_words = open_file.read().rstrip()
    all_words = all_words.split('\n')
    return random.choice(all_words)

def guess_letters():
    secret_word = pick_a_word()
    guesses = 0
    correct_guesses = 0
    list_of_guesses = set()
    guessed_word = ["_ "]*len(secret_word)
    print(secret_word)
    print_word_board(guessed_word)
    while correct_guesses != len(secret_word) and guesses < 6:
        next_guess = input("Guess my word (letter by letter) "+str(6 - guesses)+" guesses left:\n")
        if next_guess in secret_word and next_guess not in list_of_guesses:
            print(next_guess+ " is in my word!")
            for n, letter in enumerate(secret_word):
                if letter == next_guess:
                    guessed_word[n] = letter
                    correct_guesses += 1
        elif next_guess in list_of_guesses:
            print("You already guessed that letter!?")
        else:
            print("Bad luck")
            guesses += 1
        list_of_guesses.add(next_guess)
        print_word_board(guessed_word)
    if guesses >= 6 and correct_guesses != len(secret_word) :
        print("You lost!\nThe word was " + secret_word)
    else:
        print("You won after "+str(guesses)+" guesses!\nThe word was " + secret_word)
    if input("Play Again (Y/N)?: ") == "y":
        guess_letters()


if __name__ == "__main__":
    guess_letters()