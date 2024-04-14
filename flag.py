from math import ceil
def flag(size: int):
    third = size // 3
    current = 1
    for i in range(ceil(size/2)):
        for j in range(ceil(size*4)):
            if j == 0:
                print("|", end="")
            elif j == ceil(size*4) - 1:
                print("|", end="")
            elif j <= current:
                print("*", end="")
            else:
                print("=", end="")
        current += 2
        print("")
    current -= 1
    for i in range(ceil(size/2)):
        for j in range(ceil(size*4)):
            if j == 0:
                print("|", end="")
            elif j == ceil(size*4) - 1:
                print("|", end="")
            elif j <= current:
                print("*", end="")
            else:
                print(" ", end="")
        current -= 2
        print("")

flag(10)
print("")