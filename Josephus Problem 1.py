def bin_dec(n):
    count = 0
    sum = 0
    for i in n[::-1]:
        sum += int(i) * (2**count)
        count += 1
    return sum

n = int(input("Enter number of persons standing in circle: "))

n_bin = bin(n).replace("0b","")

ans = n_bin[1:]+n_bin[:1]

print(f"The Last Survivor is person {bin_dec(ans)}")