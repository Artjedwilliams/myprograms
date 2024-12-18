name =input("Enter your name: ")
print(f"Hi {name},")
deposit =eval(input("Enter the amount you want to deposit: "))

oneK = deposit // 1000
oneK_rem = deposit % 1000

fiveH = oneK_rem // 500
fiveH_rem = oneK_rem % 500

twoH = fiveH_rem // 200
twoH_rem = fiveH_rem % 200

oneH = twoH_rem // 100
oneH_rem = twoH_rem % 100

fifty = oneH_rem // 50
fifty_rem = oneH_rem % 50

twenty = fifty_rem // 20
twenty_rem = fifty_rem % 20

ten = twenty_rem // 10
ten_rem = twenty_rem % 10

five = ten_rem // 5
five_rem = ten_rem % 5

one = five_rem // 1
one_rem = five_rem % 1

print(f"Hi {name}, your deposited amount broken down into PHP denomination is as follows: ")

print(oneK, "-1000")
print(fiveH, "-500")
print(twoH, "-200")
print(oneH, "-100")
print(fifty, "-50")
print(twenty, "-20")
print(ten, "-10")
print(five, "-5")
print(one, "-1")