import random


def number_guessing():
    number = random.randint(1, 100)
    attempts = 1

    print("Welcome to the Number Guessing Game!")
    print("Enter number between 1 and 100")

    while True:
        guess = input(f"Attempt:{attempts} Enter your guess : ")
        attempts += 1

        if guess.isdigit():
            if int(guess) > 100:
                print("Please enter number below 100")

            elif int(guess) < 0:
                print("Please enter number greater than 0")

            elif int(guess) == number:
                print("Congratulations! Your guess is correct")
                break

            elif int(guess) < number:
                print("Your guess is too low")

            else:
                print("Your guess is too high")

        else:
            print("Enter integer only")


while True:
    number_guessing()
    again = input("Press Enter to play again (or type 'q' to quit): ")
    if again.lower() == "q":
        print("Thanks for playing!")
        print("-" * 30)
        print()
        break

    print("-" * 30)
    print("Game restarted! I've picked a new number")
    print()
