import random

def play_game():
    while True:
        range_top = input("Type a number larger than 0: ")
        
        if range_top.isdigit() and int(range_top) > 0:
            range_top = int(range_top)
            break
        else:
            print("Invalid input. Please type a valid number larger than 0 :/")
    
    random_number = random.randint(1, range_top)
    guesses = 0
    
    while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time :/")
            continue

        if user_guess == random_number:
            print(f"Congrats! You guessed the correct number ({random_number})!")
            break
        elif user_guess > random_number:
            print("You were above the number!! Try again !!")
        else:
            print("You were below the number!! Try again !!")

    print(f"You got it in {guesses} guesses!")

while True:
    play_game()  # Start the game
    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != 'y':
        print("Thanks for playing! Goodbye :)")
        break
