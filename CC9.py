for x in range(9):
    for y in range(x):
        print(" ", end=" ")
    for y in range(9 - x):
        print("*", end=" ")
    print()