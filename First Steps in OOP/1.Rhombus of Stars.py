def print_top_part(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for star in range(1, i):
            print('*', end=' ')
        print('*')


def print_bottom_part(n):
    for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for star in range(1, i):
            print('*', end=' ')
        print('*')


def print_rhombus(n):
    print_top_part(n)
    print_bottom_part(n)


n = int(input())
print_rhombus(n)
