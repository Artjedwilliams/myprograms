balance = 0
initial_amount = 0
name = ""

import os

def create_account():
    global name, balance
    name = input("Create an account - Enter account name: ")
    print("| Account Created |")
    while True:
        try:
            initial_deposit = float(input(f"Hi {name}, Welcome! Thank you for using our system.\nWe require an initial deposit.\nEnter amount: "))
            if initial_deposit <= 0:
                print("Amount must be positive. Try again.")
                continue
            balance = initial_deposit  # Set the initial balance
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    os.system("cls")

def denominations(amount):
    # Compute Philippine denominations for any given amount
    denominations_list = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    print("The Philippine denominations for the amount entered are as follows:")
    for denom in denominations_list:
        count = int(amount // denom)
        amount %= denom
        print(f"{denom} = {count}")

def check_balance():
    print(f"Your current balance is: ₱{balance:.2f}")

def deposit():
    global balance
    while True:
        try:
            depo = float(input("Enter the amount to deposit: "))
            if depo <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    print(f"You entered: ₱{depo:.2f}")
    denominations(depo)

    deposit_confirm = input("Would you like to deposit the entered amount? (yes/no): ").lower()
    if deposit_confirm == "yes":
        balance += depo
        print(f"Successfully deposited ₱{depo:.2f}.")
        print(f"Current balance is ₱{balance:.2f}.")
    elif deposit_confirm == "no":
        print("Deposit cancelled.")
    else:
        print("Invalid choice. Deposit cancelled.")

def withdraw():
    global balance
    while True:
        try:
            widro = float(input("Enter the amount to withdraw: "))
            if widro <= 0:
                print("Amount must be positive. Try again.")
                continue
            if widro > balance:
                print("Insufficient funds. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    balance -= widro
    print(f"Successfully withdrew ₱{widro:.2f}.")
    print(f"Current balance is ₱{balance:.2f}.")

def action():
    os.system("cls")
    print(f"Hi {name}! What would you like to do today?")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. End program")

# Main Program
create_account()

while True:
    action()
    choice = input("Select an option: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        os.system("cls")
        print("Thank you for using our services. :)")
        break
    else:
        print("Invalid choice. Please try again.")