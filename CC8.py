summation = 0
even = 0
odd = 0
for x in range(1,11):
    num = eval(input(f"Input #{x}: "))
    summation += num

    if num % 2 == 0:
        even += num
    else:
        odd += num
print(f"The SUM of all the numbers is {summation}")
print(f"The SUM of all EVEN numbers is {even}")
print(f"The SUM of all ODD number is {odd}")