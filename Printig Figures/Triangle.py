def upper(num):
    for row in range(1, num + 1):
        for col in range(num):
            print(" " * (num - row) + "* " * row)
            break


n = int(input())
upper(n)