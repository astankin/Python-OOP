# with open("text.txt", "a") as file:
#     file.write("Hello World!\n")
count = 0
with open("text.txt", "r") as file:
    for line in file:
        count += 1

print(count)
counter = 0
with open("text.txt", "r") as file:
    for line in file:
        for char in line:
            if char.isupper():
                counter += 1

print(counter)



