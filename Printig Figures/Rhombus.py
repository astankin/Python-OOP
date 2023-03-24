def upper(num):
    for row in range(1, num + 1):
        for col in range(num):
            print(" " * (num - row) + "* " * row)
            break


def bottom(num):
    for row in range(1, num):
        for col in range(num):
            print(" " * row + "* " * (num - row))
            break


def print_figure(num):
    upper(num)
    bottom(num)


n = int(input())
print_figure(n)