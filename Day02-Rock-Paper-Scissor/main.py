import random


def inputs():
    choice_map = {"r": "rock", "p": "paper", "s": "scissor"}

    while True:
        comp_choice = random.choice(["rock", "paper", "scissor"])
        user_option = (
            input("Enter r for rock, p for paper & s for scissor: ").strip().lower()
        )

        if user_option in choice_map:
            user_choice = choice_map[user_option]
            return comp_choice, user_choice

        else:
            print("Invalid input. Please enter 'r' or 'p' or 's'")


def winner(comp_choice, user_choice):

    comp_win_combo = {"rock": "scissor", "paper": "rock", "scissor": "paper"}

    if comp_win_combo[comp_choice] == user_choice:
        return "Computer Wins"
    elif comp_choice == user_choice:
        return "Its draw"
    else:
        return "You Win"


def game():
    comp, user = inputs()
    print(f"You chose {user.title()} while computer chose {comp.title()}")
    print(winner(comp, user))


game()
