name = input("Enter your name: ")
age = eval(input("Enter your age: "))

if age >= 1 and age <= 8:
    print(f" Hi {name}, you are a Toddler")
elif age >= 9 and age <= 14:
    print(f" Hi {name}, you are a Pre-teen")
elif age >= 15 and age <= 18:
    print(f" Hi {name}, you are a Teenager")
elif age >= 19 and age <=27:
    print(f" Hi {name}, you are in your Early Adulthood")
elif age >= 28 and age <=44:
    print(f" Hi {name}, you are in your Middle Age")
elif age >= 45 and age <=59:
    print(f" Hi {name}, you are in your Post Adulthood")
elif age >= 60:
    print(f"Hi {name}, you are a Senior")
else:
    print("Invalid Age")