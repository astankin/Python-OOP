n = int(input())
count = 65
for i in range(n + 1):
    for j in range(i):
        print(chr(count), end=" ")
        count += 1
    print()