import random

def int_to_base(x, base):
    # Converts an integer x to the specified base.
    if x == 0:
        return "0", ["No conversion needed for zero."]

    digits = []
    steps = []

    original_number = x
    while x:
        remainder = int(x % base)
        digits.append(remainder)
        steps.append(f"{x} ÷ {base} = {x // base}, remainder {remainder}")
        x //= base

    steps.reverse()
    return ''.join(str(x) for x in digits[::-1]), steps

def explain_conversion(original_number, original_base, converted_number, target_base):
    # Provides a detailed step-by-step explanation of numeral system conversion.
    numeral_systems = {
        2: "Binary",
        10: "Decimal",
        8: "Octal",
        16: "Hexadecimal"
    }

    # Convert original and converted numbers to their respective numeral systems
    original_in_base = int_to_base(original_number, original_base)
    converted_in_target = int_to_base(converted_number, target_base)

    # Print initial information about the conversion process
    print(f"To convert the {numeral_systems[original_base]} number")
    print(f"{original_in_base[0]} in {numeral_systems[original_base]}")
    print(f"to {numeral_systems[target_base]} (base {target_base}), we follow these steps:")
    print()
    print(f"1. Write down the {numeral_systems[original_base]} number: Start with the {numeral_systems[original_base]} number")
    print(f"{original_in_base[0]}")
    print()

    # Explain how each digit in the original numeral system contributes to its value
    print(f"2. Identify the positional values: Each digit in the {numeral_systems[original_base]} number represents a power of {original_base},")
    print(f"starting from the rightmost digit with {original_base**0} ({original_in_base[0][-1]}) and increasing by 1 for each subsequent position to the left.")
    print()

    print(f"For {original_in_base[0]}:")
    for i in range(len(original_in_base[0])):
        power = len(original_in_base[0]) - i - 1
        digit_value = int(original_in_base[0][i], original_base) * (original_base ** power)
        print(f"{original_in_base[0][i]} × {original_base}^{power} = {original_in_base[0][i]} × {original_base ** power} = {digit_value}")
    print()

    # Sum up the contributions to calculate the decimal value
    print(f"3. Calculate the decimal value: Multiply each {numeral_systems[original_base]} digit (either 0 or 1) by its corresponding power of {original_base}")
    print(f"and sum these values.")
    print()

    print(f"For {original_in_base[0]}:")
    print(f"{'+'.join([f'{int(original_in_base[0][i], original_base)} × {original_base}^{len(original_in_base[0])-i-1}' for i in range(len(original_in_base[0]))])}")
    print(f"= {'+'.join([str(int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1))) for i in range(len(original_in_base[0]))])}")
    print()

    print(f"Add these values together: Sum up all the values calculated in the previous step.")
    print()
    print(f"{'+'.join([str(int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1))) for i in range(len(original_in_base[0]))])}")
    print(f"= {sum([int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1)) for i in range(len(original_in_base[0]))])}")
    print()

    # Print the final converted value in the target numeral system
    print(f"Therefore, {original_in_base[0]} in {numeral_systems[original_base]} is equivalent to {converted_in_target[0]} in {numeral_systems[target_base]}.")

def random_number_conversion():
    # Allows the user to choose between random numeral system conversion or selecting numeral systems manually.
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
        from_base = random.choice(list(numeral_systems.keys()))  # Randomly choose a numeral system
        to_base = random.choice(list(numeral_systems.keys()))
        while to_base == from_base:
            to_base = random.choice(list(numeral_systems.keys()))  # Ensure from_base and to_base are different

        random_number = random.randint(0, (2**10)-1)  # Generate a random number suitable for binary (up to 1023)

        # Display initial information
        print(f"\nRandomly chosen numeral system: Convert from {numeral_systems[from_base]} to {numeral_systems[to_base]}")
        print(f"The randomly generated number is: {int_to_base(random_number, from_base)[0]} in {numeral_systems[from_base]}")

        # Calculate the correct answer
        correct_answer = int_to_base(random_number, to_base)[0]

        # Ask user for their answer
        user_answer = input(f"What is {int_to_base(random_number, from_base)[0]} in {numeral_systems[to_base]}? ")

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")

        # Show the explanation regardless of the answer
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

        random_number = random.randint(0, (2**10)-1)  # Generate a random number suitable for binary (up to 1023)

        # Display initial information
        print(f"\nYou chose numeral systems: Convert from {numeral_systems[from_base]} to {numeral_systems[to_base]}")
        print(f"The randomly generated number is: {int_to_base(random_number, from_base)[0]} in {numeral_systems[from_base]}")

        # Calculate the correct answer
        correct_answer = int_to_base(random_number, to_base)[0]

        # Ask user for their answer
        user_answer = input(f"What is {int_to_base(random_number, from_base)[0]} in {numeral_systems[to_base]}? ")

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")

        # Show the explanation regardless of the answer
        converted_number = int(int_to_base(random_number, from_base)[0], from_base)
        explain_conversion(random_number, from_base, converted_number, to_base)

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

# Run the function
random_number_conversion()
