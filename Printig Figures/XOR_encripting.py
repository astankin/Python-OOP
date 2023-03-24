message = "ATTACKPEARLHARBOR"
key = "TIGER"
new_message = ""
for i in range(len(message)):
    new_message += chr((ord(key[i % (len(key))]) ^ ord(message[i])) + 65)

print(new_message)
