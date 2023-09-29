"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Gregor Musteata
email: MusteataG@seznam.cz
discord: Gregor M.#7392
"""

import random
import time

#tajné číslo
def generate_secret_number():
    digits = random.sample(range(1,10),4)
    return ''.join(map(str, digits))

#vyhodnocení
def evaluate_guess(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

print("Hi there!")
print("_"*50)
print("I've generated a random 4-digit number for you")
print("Let's play a bulls and cows game.")
print("_"*50)


#time a pokusy
start_time = None
attempts = 0
guessed_numbers = []
secret_number = None
#hra
def play_game():
    global attempts, start_time, guessed_numbers, secret_number
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    guessed_numbers = []
if __name__ == "__main__":
    play_game()
    start_time = time.time()

while True:
    guess = input("Enter a number: ")

    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
        print("Invalid input. Please enter a 4-digit number with unique digits.")
        continue
    if guess in guessed_numbers:
        print("You've already guessed that number. Try a different one.")
        continue

    attempts += 1
    guessed_numbers.append(guess)
    bulls, cows = evaluate_guess(secret_number, guess)
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
    print("_"*50)

    if bulls == 4:
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"You guassed the right number in {attempts} {'guess' if attempts == 1 else 'guesses'} "
              f"and it took you {minutes} minute{'s' if minutes !=1 else''} and {seconds} second{'s' if seconds != 1 else ''}")
        break


