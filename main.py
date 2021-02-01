
import random
from art import logo

print(logo)

lives = 0

level = input("Select the level of the game: type 'hard' or 'easy': ")

if level == "easy":
    lives += 10
else:
    lives += 5


picked_number = random.randint(0, 100)

print(f"Shhh, the pickes number is {picked_number}.")

still_playing = True

while still_playing:
    
    print(f"You have {lives} guesses.")
    guessed_number = int(input("Guess the number: "))
    lives -= 1

    if lives == 0:
        print("No more guesses, you lose.")
        still_playing = False
    elif guessed_number < picked_number:
        print("Too low")
    elif guessed_number > picked_number:
        print("Too high")
    else:
        print(f"Well done! {guessed_number} is the correct number.")
        still_playing = False
