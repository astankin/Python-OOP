from collections import deque

alphabet = [chr(x) for x in range(65, 91)]
shuffle = deque([chr(x) for x in range(65, 91)])
message = "ATTACK"
key = "LEMON"
new_message = ""
for i in range(len(message)):
    while True:
        if shuffle[0] == key[i % len(key)]:
            new_message += shuffle[alphabet.index(message[i])]
            break
        shuffle.rotate()
print(new_message)
