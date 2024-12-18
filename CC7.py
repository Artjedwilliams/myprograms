Tax_rate = 0.123
Discount_rate = 0.038
Senior_discount_rate = 0.123

# User input
name = input("Enter your name: ")
didBUY = input("Did you purchase grocery today? (y/n): ")
print()
if didBUY.lower() == "y":
    product = input("What product did you purchase? ")
    product_price = float(input("What was the price of the item? "))
    print()
    # TAX
    taxed_price = product_price + product_price * Tax_rate
    print(f"A tax of {Tax_rate * 100}% is applied. The new price (with tax) is {round(taxed_price, 2)}")

    # Initialize final price as taxed price
    final_price = taxed_price

    # Discount eligibility
    if product_price > 4000:
        discount = product_price * Discount_rate
        discounted_price = product_price - discount
        print(f"Since the original price of the product cost more than 4000, a discount of {Discount_rate * 100}% is applied to the original price.")

        # Update final price with discount
        final_price = discounted_price + (discounted_price * Tax_rate)
        print(f"Final price (with tax and discount) is {round(final_price, 2)}")
    print()
    # Ask age to apply senior discount or not
    age = int(input("Enter your age: "))

    # Senior Discount
    if 60 <= age <= 150:
        senior_discount = final_price * Senior_discount_rate
        final_price -= senior_discount
        print(f"You are eligible for the {Senior_discount_rate * 100}% senior discount.")

    else:
        print("No senior discount.")

    # Final price after all conditions
    print(f"Total amount to pay is {round(final_price, 2)}")
    print()
    # Ask for payment and calculate change
    payment = float(input("Enter payment amount: "))
    change = payment - final_price

    # If payment is insufficient
    if change < 0:
        print("Insufficient payment.")
        payment = float(input("Enter payment amount: "))
        change = payment - final_price
        print(f"Change: {round(change, 2)}")
    else:
        print(f"Change: {round(change, 2)}")
else:
    print("Okay, bye! LOL")