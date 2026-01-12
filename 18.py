# Create a program that will play the “cows and bulls” game with the user.
#  The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#  For every digit that the user guessed 
# correctly in the correct place, they have a “cow”. For every digit the user 
# guessed correctly in the wrong place is a “bull.” Every time the user makes 
# a guess, tell them how many “cows” and “bulls” they have. Once the user 
# guesses the correct number, the game is over. Keep track of the number of 
# guesses the user makes throughout the game and tell the user at the end.

import random

def generate_number():
    # Generate a random 4-digit number as a string
    return str(random.randint(1000, 9999))


def play_game():
    secret = generate_number()
    attempts = 0

    print("🐮🐂 Welcome to the Cows and Bulls Game!")
    print("I have generated a 4-digit number. Try to guess it!")
    # print(secret)

    while True:
        guess = input("Enter your 4-digit guess: ")

        # Validate input
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input! Please enter exactly 4 digits.")
            continue

        attempts += 1
        cows = 0
        bulls = 0

        # Count cows and bulls
        for i in range(4):
            if guess[i] == secret[i]:
                cows += 1
            elif guess[i] in secret:
                bulls += 1

       
        print(f"Cows: {cows}, Bulls: {bulls}")
        # Check win condition
        if cows == 4:
            print("🎉 Congratulations! You guessed the correct number!")
            print(f"You took {attempts} guesses.")
            
            break


if __name__ == "__main__":
    play_game()
