def reverse_text(string):
    i = 1
    while i <= len(string):
        yield string[-i]
        i += 1


for char in reverse_text("step"):
    print(char, end='')
