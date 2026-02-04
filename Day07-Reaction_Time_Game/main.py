import time
from random import random


def play_game():
    input("Press 'Enter' & wait for 'GO' signal!")
    time.sleep(random.uniform(1, 5))
    print()
    print("GO!")

    start = time.perf_counter()
    input("")
    end = time.perf_counter()

    total = end - start
    if total < 0.1:
        print("Too fast! Disqualified.")
        print()
    else:
        print(f"You took {total*1000:.0f} milliseconds to react.")
        print()


while True:
    play_game()
    again = input("Press Enter to play again (or type 'q' to quit): ")
    if again.lower() == "q":
        print("Thanks for playing!")
        print("-" * 30)
        print()
        break
    print("-" * 30)
    print()
