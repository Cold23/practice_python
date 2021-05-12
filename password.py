import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for guess in itertools.product(chars,repeat = 6): #like a double iteration 
        attempts += 1
        guess = ''.join(guess)
        if guess == real:
            return 'password is {}. found in {} guesses.'.format(guess, attempts)

if __name__ == "__main__":
    print(guess_password('ftestpass'))