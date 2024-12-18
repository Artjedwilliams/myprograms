#decision structures/conditional statements 

password = "password"

mypassword = input("Enter password: ")

if password == mypassword:
    print("| Access granted |")


elif mypassword == "password1":
    print("| Access granted |") 

elif mypassword == "password2":
    print("| Access granted |")

else:
    print("| Access denied |")