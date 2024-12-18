import sys
import time

def sp(text, delay=0.070):
    """Prints text slowly for better readability."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def sp1(text, delay=0.010):
    """Prints text slowly for better readability."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print()
sp("   Welcome to my program!")  # Program start message

def main_menu():
    """Main menu for user selection."""
    while True:
        print()
        sp1("         |Options|")
        print()
        sp1("1. Denominations Breakdown - Calculate how a given amount can be divided into Philippine currency denominations.")
        sp1("2. Calculator - Perform basic arithmetic operations.")
        sp1("3. Pass or Fail Checker - Determine if a student passed based on grades.")
        sp1("4. Age Classification - Classify an individual into age groups.")
        sp1("5. Temperature Converter - Convert temperatures between Celsius and Fahrenheit.")
        sp1("6. Shapes - Display geometric shapes.")
        sp1("7. Exit - Quit the program.")
        print()

        try:
            choice = int(input("   Select an option (1-7): "))
            if choice == 1:
                print("\n--- Denominations Breakdown ---")
                print("This will calculate how to break down your amount into Philippine currency bills.")
                denominations()
            elif choice == 2:
                print("\n--- Calculator ---")
                print("You can perform basic arithmetic operations here.")
                calculator()
            elif choice == 3:
                print("\n--- Pass or Fail Checker ---")
                print("Input grades to check if you passed or failed the course.")
                pass_or_fail()
            elif choice == 4:
                print("\n--- Age Classification ---")
                print("Classify yourself into age groups based on your age.")
                age_classification()
            elif choice == 5:
                print("\n--- Temperature Converter ---")
                print("Convert temperatures between Celsius and Fahrenheit.")
                temperature_converter()
            elif choice == 6:
                print("\n--- Shapes ---")
                print("Display geometric shapes like diamond, triangle, or square.")
                shapes()
            elif choice == 7:
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

def denominations():
    print("\nThis feature breaks down an amount into Philippine currency denominations.")
    deposit = eval(input("Enter the amount you want to break down to Philippine denomination: "))
    
    # Calculation and printing denominations
    oneK = deposit // 1000
    fiveH = (deposit % 1000) // 500
    twoH = (deposit % 500) // 200
    oneH = (deposit % 200) // 100
    fifty = (deposit % 100) // 50
    twenty = (deposit % 50) // 20
    ten = (deposit % 20) // 10
    five = (deposit % 10) // 5
    one = (deposit % 5) // 1

    sp1("\nHere is the breakdown of your amount into denominations:")
    print(f"{oneK} x PHP 1000")
    print(f"{fiveH} x PHP 500")
    print(f"{twoH} x PHP 200")
    print(f"{oneH} x PHP 100")
    print(f"{fifty} x PHP 50")
    print(f"{twenty} x PHP 20")
    print(f"{ten} x PHP 10")
    print(f"{five} x PHP 5")
    print(f"{one} x PHP 1")

def calculator():
    while True:
        sp1("\n--- Calculator ---")
        sp1("Select an operation:")
        sp1("1. Addition")
        sp1("2. Subtraction")
        sp1("3. Multiplication")
        sp1("4. Division")
        sp1("5. Exponentiation")
        sp1("6. Remainder (Modulo)")
        sp1("7. Floor Division")
        sp1("8. Exit Calculator")

        try:
            choice = int(input("\nChoose an operation (1-8): "))
            if choice == 8:
                print("\nExiting the calculator.")
                break
            num1 = eval(input("Enter the first number: "))
            num2 = eval(input("Enter the second number: "))

            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Division by zero is not allowed.")
            elif choice == 5:
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")
            elif choice == 6:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == 7:
                print(f"Result: {num1} // {num2} = {num1 // num2}")
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter valid numbers.")

def pass_or_fail():
    print("\nCalculate your final grade to see if you passed!")
    prelim = eval(input("Enter your prelim grade: "))
    midterm = eval(input("Enter your midterm grade: "))
    semifinal = eval(input("Enter your semifinal grade: "))
    final = eval(input("Enter your final grade: "))
    quiz = eval(input("Enter your quiz grade: "))
    project = eval(input("Enter your project grade: "))

    final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
    print(f"\nYour final grade is: {final_grade:.2f}")
    if final_grade >= 75:
        print("Congratulations! You passed.")
    else:
        print("Sorry, you failed.")

# Add printed explanations for other features like age_classification, temperature_converter, and shapes similarly.

# Run the main menu
main_menu()
