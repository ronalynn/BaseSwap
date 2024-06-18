import random

def int_to_base(x, base):
    """
    Converts an integer x to the specified base.
    
    Args:
        x (int): The number to convert.
        base (int): The base to convert to.
    
    Returns:
        tuple: A tuple containing the converted number as a string and the steps taken as a list of strings.
    """
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
    return ''.join(str(digit) for digit in digits[::-1]), steps

def explain_conversion(original_number, original_base, converted_number, target_base):
    """
    Provides a detailed step-by-step explanation of numeral system conversion.
    
    Args:
        original_number (int): The number in the original base.
        original_base (int): The original base.
        converted_number (int): The number in the target base.
        target_base (int): The target base.
    """
    numeral_systems = {
        2: "Binary",
        10: "Decimal",
        8: "Octal",
        16: "Hexadecimal"
    }

    original_in_base = int_to_base(original_number, original_base)
    converted_in_target = int_to_base(converted_number, target_base)

    print("**** CONVERSION EXPLANATION ****\n")
    print(f"We're converting the {numeral_systems[original_base]} number {original_in_base[0]} to {numeral_systems[target_base]}.\n")
    
    explain_positional_values(original_in_base, original_base)
    explain_decimal_conversion(original_in_base, original_base)
    
    if target_base != 10:
        explain_base_conversion(converted_in_target, target_base)
        print(f"Therefore, {original_in_base[0]} in {numeral_systems[original_base]} is equivalent to {converted_in_target[0]} in {numeral_systems[target_base]}.")
    else:
        decimal_sum = calculate_decimal_value(original_in_base[0], original_base)
        print(f"Therefore, {original_in_base[0]} in {numeral_systems[original_base]} is equivalent to {decimal_sum} in {numeral_systems[target_base]}.")

def explain_positional_values(original_in_base, original_base):
    print("1. Understanding the digits in the original number:")
    print(f"Each digit in {original_in_base[0]} represents a power of {original_base}.")
    print(f"The rightmost digit is multiplied by {original_base}^0, the next by {original_base}^1, and so on.\n")
    
    print(f"For {original_in_base[0]}:")
    for i in range(len(original_in_base[0])):
        power = len(original_in_base[0]) - i - 1
        digit_value = int(original_in_base[0][i], original_base) * (original_base ** power)
        print(f"{original_in_base[0][i]} × {original_base}^{power} = {original_in_base[0][i]} × {original_base ** power} = {digit_value}")
    print()

def explain_decimal_conversion(original_in_base, original_base):
    print("2. Calculating the Decimal (base 10) value:")
    print("Add up all the values we just calculated.\n")
    
    decimal_sum = calculate_decimal_value(original_in_base[0], original_base)
    print(f"{'+'.join([f'{int(original_in_base[0][i], original_base)} × {original_base}^{len(original_in_base[0])-i-1}' for i in range(len(original_in_base[0]))])}")
    print(f"= {'+'.join([str(int(original_in_base[0][i], original_base) * (original_base ** (len(original_in_base[0])-i-1))) for i in range(len(original_in_base[0]))])}")
    print(f"= {decimal_sum}\n")

def explain_base_conversion(converted_in_target, target_base):
    print(f"3. Converting Decimal to the target base:")
    print(f"We repeatedly divide the number by {target_base} and record the remainders.\n")
    
    for step in converted_in_target[1]:
        print(step)
    print()

def calculate_decimal_value(number_str, base):
    return sum(int(number_str[i], base) * (base ** (len(number_str) - i - 1)) for i in range(len(number_str)))

def random_number_conversion():
    """
    Initiates a numeral system conversion game where the user can either choose the numeral systems or have them selected randomly.
    """
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
        from_base, to_base = select_random_bases(numeral_systems)
    elif choice == '2':
        from_base, to_base = select_user_bases(numeral_systems)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    random_number = random.randint(0, (2**10)-1)
    number_in_from_base = int_to_base(random_number, from_base)[0]

    print(f"\nYou chose to convert from {numeral_systems[from_base]} to {numeral_systems[to_base]}")
    print(f"The randomly generated number is: {number_in_from_base} in {numeral_systems[from_base]}")

    correct_answer = int_to_base(random_number, to_base)[0]

    user_answer = input(f"What is {number_in_from_base} in {numeral_systems[to_base]}? ")

    if user_answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.\n")

    converted_number = int(number_in_from_base, from_base)
    explain_conversion(random_number, from_base, converted_number, to_base)

def select_random_bases(numeral_systems):
    from_base = random.choice(list(numeral_systems.keys()))
    to_base = random.choice(list(numeral_systems.keys()))
    while to_base == from_base:
        to_base = random.choice(list(numeral_systems.keys()))
    return from_base, to_base

def select_user_bases(numeral_systems):
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
        else:
            print("Invalid choice. Please enter 2, 10, 8, or 16.")
        to_base = int(input("Enter the numeral system you want to convert to (2, 10, 8, 16): "))

    return from_base, to_base

# Run the function
random_number_conversion()
