import random

def int_to_base(x, base):
    # Converts an integer x to the specified base.
    if x == 0:
        return "0", ["No conversion needed for zero."]

    digits = []
    steps = []

    while x:
        remainder = x % base
        digits.append(remainder)
        steps.append(f"{x} ÷ {base} = {x // base}, remainder {remainder}")
        x //= base

    steps.reverse()
    return ''.join(str(x) for x in digits[::-1]), steps

def explain_conversion(original_number, original_base, converted_number, target_base):
    numeral_systems = {
        2: "Binary",
        10: "Decimal",
        8: "Octal",
        16: "Hexadecimal"
    }

    original_in_base = int_to_base(original_number, original_base)
    converted_in_target = int_to_base(converted_number, target_base)

    print("**** CONVERSION EXPLANATION ****")
    print()
    print(f"We're converting the {numeral_systems[original_base]} number {original_in_base[0]} to {numeral_systems[target_base]}.")
    print()

    print("1. Understanding the digits in the original number:")
    print(f"Each digit in {original_in_base[0]} represents a power of {original_base}.")
    print(f"The rightmost digit is multiplied by {original_base}^0, the next by {original_base}^1, and so on.")
    print()

    print(f"For {original_in_base[0]}:")
    for i in range(len(original_in_base[0])):
        power = len(original_in_base[0]) - i - 1
        digit_value = int(original_in_base[0][i], original_base) * (original_base ** power)
        print(f"{original_in_base[0][i]} × {original_base}^{power} = {original_in_base[0][i]} × {original_base ** power} = {digit_value}")
    print()

    print(f"2. Calculating the Decimal (base 10) value:")
    print(f"Add up all the values we just calculated.")
    print()

    decimal_sum = sum([int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1)) for i in range(len(original_in_base[0]))])
    print(f"{'+'.join([f'{int(original_in_base[0][i], original_base)} × {original_base}^{len(original_in_base[0])-i-1}' for i in range(len(original_in_base[0]))])}")
    print(f"= {'+'.join([str(int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1))) for i in range(len(original_in_base[0]))])}")
    print(f"= {decimal_sum}")
    print()

    if target_base != 10:
        print(f"3. Converting Decimal to {numeral_systems[target_base]}:")
        print(f"Now, we convert the decimal value {decimal_sum} to {numeral_systems[target_base]}.")
        print(f"We repeatedly divide the number by {target_base} and record the remainders.")
        print()

        for step in int_to_base(decimal_sum, target_base)[1]:
            print(step)
        print()

        print(f"Therefore, {original_in_base[0]} in {numeral_systems[original_base]} is equivalent to {converted_in_target[0]} in {numeral_systems[target_base]}.")
    else:
        print(f"Therefore, {original_in_base[0]} in {numeral_systems[original_base]} is equivalent to {decimal_sum} in {numeral_systems[target_base]}.")

def random_number_conversion():
    numeral_systems = {
        2: "Binary",
        10: "Decimal",
        8: "Octal",
        16: "Hexadecimal"
    }

    print("Select a game mode:")
    print("(1) Select the numeral system for me")
    print("(2) I want to choose the numeral system")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        from_base = random.choice(list(numeral_systems.keys()))  
        to_base = random.choice(list(numeral_systems.keys()))
        while to_base == from_base:
            to_base = random.choice(list(numeral_systems.keys()))  

        random_number = random.randint(0, (2**10)-1)  

        print(f"\nRandomly chosen numeral system: Convert from {numeral_systems[from_base]} to {numeral_systems[to_base]}")
        print(f"The randomly generated number is: {int_to_base(random_number, from_base)[0]} in {numeral_systems[from_base]}")

        correct_answer = int_to_base(random_number, to_base)[0]

        user_answer = input(f"What is {int_to_base(random_number, from_base)[0]} in {numeral_systems[to_base]}?: ")

        if user_answer == correct_answer:
            print()
            print("Correct!")
            print()
        else:
            print()
            print(f"Wrong. The correct answer is {correct_answer}.")
            print()

        converted_number = int(int_to_base(random_number, from_base)[0], from_base)
        explain_conversion(random_number, from_base, converted_number, to_base)

    elif choice == '2':
        print("\nAvailable numeral systems:")
        for key, value in numeral_systems.items():
            print(f"({key}) {value}")

        from_base = int(input("Enter the numeral system you want to start with (2, 10, 8, 16): "))
        while from_base not in numeral_systems:
            print("Invalid choice. Please enter 2, 10, 8, or 16.")
            from_base = int(input("Enter the numeral system you want to start with (2, 10, 8, 16): "))

        to_base = int(input("Enter the numeral system you want to convert to (2, 10, 8, 16): "))
        while to_base not in numeral_systems or to_base == from_base:
            if to_base == from_base:
                print("To base must be different from from base.")
            print("Invalid choice. Please enter 2, 10, 8, or 16.")
            to_base = int(input("Enter the numeral system you want to convert to (2, 10, 8, 16): "))

        random_number = random.randint(0, (2**10)-1)  

        print(f"\nYou chose numeral systems: Convert from {numeral_systems[from_base]} to {numeral_systems[to_base]}")
        print(f"The randomly generated number is: {int_to_base(random_number, from_base)[0]} in {numeral_systems[from_base]}")

        correct_answer = int_to_base(random_number, to_base)[0]

        user_answer = input(f"What is {int_to_base(random_number, from_base)[0]} in {numeral_systems[to_base]}? ")

        if user_answer == correct_answer:
            print()
            print("Correct!")
            print()
        else:
            print()
            print(f"Wrong. The correct answer is {correct_answer}.")
            print()

        converted_number = int(int_to_base(random_number, from_base)[0], from_base)
        explain_conversion(random_number, from_base, converted_number, to_base)

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

random_number_conversion()
