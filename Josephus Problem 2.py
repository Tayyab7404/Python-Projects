n = int(input("Enter number of persons standing in circle: "))

k = int(input("Enter value of count: "))

C = [x for x in range(1,n+1)]

while len(C)>1:
    I = (k % len(C) - 1)

    if I >= 0:
        C = C[I+1:] + C[:I]
    else:
        C = C[:-1]

print(f"The Last Survivor is person {C[0]}")