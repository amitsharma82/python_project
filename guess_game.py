import random

random_number = random.randint(1, 10)
guess = None


while True:
    guess = input("Pick the number between 1 to 10: ")
    guess = int(guess)

    if guess < random_number:
        print("your choice is too low")

    elif guess > random_number:
        print("Your choice is too high")

    else:
        print("You Won!")
        print(f" Randam choice is {random_number}")
        play_again = input("Do  you like to play again (y/n): ")

        if play_again.lower() == 'y':
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("thanks for playing")
            break
