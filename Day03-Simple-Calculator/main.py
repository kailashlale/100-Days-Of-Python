first = input("Enter first number: ")
second = input("Enter second number: ")
operand = input("Enter + - / * ")

operand_set = {"+": "Sum", "-": "Subtraction", "*": "product", "/": "Division"}

try:
    num1 = float(first)
    num2 = float(second)

    if operand in operand_set:
        try:
            if operand == "+":
                result = num1 + num2
            elif operand == "-":
                result = num1 - num2
            elif operand == "/":
                result = num1 / num2
            else:
                result = num1 * num2

        except ZeroDivisionError:
            print("Second number cannot be zero if operand is '/' (division)")

        else:
            if result % 1 == 0:
                final_result = int(result)
            else:
                final_result = f"{result:.2f}"
            print(f"{operand_set[operand]} of {first} and {second} is {final_result}")

    else:
        print("Invalid operand")

except ValueError:
    print("Both input should be numeric only")
