# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def print_triangle(num):
    n = 1
    for row in range(1, num + 1):
        nums = []
        nums[:0] = (str(n)*row)
        print(" ".join(nums))
        n += 1


number = int(input())
print_triangle(number)

###################
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4


n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(j, end=" ")
    print()

#################################

# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input())
count = 1
for i in range(n):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

############################

# A
# B C
# D E F
# G H I J

n = int(input())
count = 65
for i in range(n):
    for j in range(i):
        print(chr(count), end=" ")
        count += 1
    print()

##################################
# 5 input
# A
# B B
# C C C
# D D D D
# E E E E E

n = int(input())
count = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(count), end=" ")
    count += 1
    print()

