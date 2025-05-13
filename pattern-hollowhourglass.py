n = 5

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        if j == 0 or j == i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        if j == 0 or j == i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
