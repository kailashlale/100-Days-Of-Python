import random
import string


def get_length():
    pass_length = input("Enter desired password length(8-32): ")
    try:
        length = int(pass_length)

    except ValueError:
        print("Enter numeric value without any symbols")
        return get_length()

    if 8 <= length <= 32:
        return length

    print("Error : Enter password length between 8 and 32")
    return get_length()


def sym_input(length_val):
    symbol = input("Include symbols (y/n): ").strip().lower()
    if symbol == "y":
        try:
            percent_syb = input("Percentage of symbol (1-40): ").replace("%", "")
            percent_symbol = int(percent_syb)

            if 1 <= percent_symbol <= 40:
                return max(1, int(length_val * percent_symbol / 100))

            print("Value must be between 1 and 40")
            return sym_input(length_val)

        except ValueError:
            print("Enter value between 0 to 40 without '%' symbol")
            return sym_input(length_val)

    return 0


def num_input(length_val):
    number = input("Include numbers (y/n): ").strip().lower()
    if number == "y":
        try:
            percent_num = input("Percentage of number (1-40): ").replace("%", "")
            percent_number = int(percent_num)
            if 1 <= percent_number <= 40:
                return max(1, int(length_val * percent_number / 100))

            print("Value must be between 1 and 40")
            return num_input(length_val)

        except ValueError:
            print("Enter value between 0 to 40 without '%' symbol")
            return num_input(length_val)

    return 0


def randomize(l_count, s_count, n_count):
    str_list = random.choices(string.ascii_letters, k=l_count)
    num_list = random.choices(string.digits, k=n_count)
    syb_list = random.choices(string.punctuation, k=s_count)
    return str_list + num_list + syb_list


def generator():
    total_length = get_length()
    symbols = sym_input(total_length)
    numbers = num_input(total_length)
    letters = max(0, total_length - symbols - numbers)

    print("Letters:", letters, "Symbols:", symbols, "Numbers:", numbers)
    pass_list = randomize(letters, symbols, numbers)
    random.shuffle(pass_list)
    password = "".join(pass_list)
    print("Password :", password)


generator()
