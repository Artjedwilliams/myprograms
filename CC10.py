for a in range(1,6):
    for b in range(6,a,-1):
        print(" ",end=" ")
    for c in range(0,a,+1):
        print("*",end=" ")
    for d in range(0,a,+1):
        print("*",end=" ")
    print()

for a in range(1,6):
    for b in range(0,a,+1):
        print(" ",end=" ")
    for c in range(6,a,-1):
        print("^",end=" ")
    for d in range(6,a,-1):
        print("^",end=" ")
    print()
