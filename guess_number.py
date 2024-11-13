import random

# Generate a random num between 1 and 100
secret_number = random.randint(1, 100)
tries = 0
max_tries = 10

print("Welcome to the Guess the Number game!")
print(f"You have {max_tries} tries to guess a number between 1 and 100.")

while tries < max_tries:
    # Ask the player to guess the num
    guess = input("\nEnter a number: ")
    
    # Validate that the input is a valid num
    if not guess.isdigit():
        print("Please enter numbers only.")
        continue
    
    guess = int(guess)
    tries += 1
    
    # Compare the numbers and give feedback to the player
    if guess < secret_number:
        print("The number is higher!")
    elif guess > secret_number:
        print("The number is lower!")
    else:
        print(f"\nCongratulations! You guessed it in {tries} tries!")
        break
        
    # Show remaining tries to the player
    print(f"You have {max_tries - tries} tries left")

# Game over message if player runs out of tries 
if tries == max_tries and guess != secret_number:
    print(f"\nGame Over. The number was {secret_number}")