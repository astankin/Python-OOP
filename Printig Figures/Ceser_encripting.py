message = input()
new_message = ""
for char in message:
    new_char = 0
    if ord(char) + 3 > 90:
        new_char = 64 + (3 - (90 - ord(char)))
    else:
        new_char = ord(char) + 3
    new_message += chr(new_char)

print(new_message)