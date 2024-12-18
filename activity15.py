import os
go = True
nt = 0
while go:
    ask = input("Do you want to print more triangles? (yes/no)    ")

    if ask.lower() == "no":
        print("Okay, no more triangles")
        break

    elif ask.lower() == "yes":
        os.system('cls')
        nt += 1
        for a in range(1,6):
            for b in range(1,nt + 1):
                for c in range(1,a + 1):
                    print("*",end=" ")
                for d in range(6,a,-1):
                    print(" ",end=" ")
                print(end=" ")
            print()
        continue
    else:
        print("Invalid input")
        print("Valid input: yes/no ")
