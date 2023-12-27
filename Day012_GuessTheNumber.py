logo = """
_____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
                                                                          """

print(logo)
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy or hard: ").lower()
number = random.randint(1,100)
if difficulty == "easy":
    attempts = 10
if difficulty == "hard":
    attempts = 5
won = False
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    elif guess == number:
        won = True
        print("You guessed the number")                
        break
    attempts -=1    
if won:
    print("Congratulations you win")
else:
    print(f"You've run out of guesses, you lose. \n Your number was {number}")        