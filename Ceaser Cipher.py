text = input("Enter Plain Text: ")
length_p = len(text)

kn = int(input("Enter Pattern: "))
enc=''
# Encryption Code
A = ""

for i in range(length_p):
    if text[i].isupper():
        enc += chr((ord(text[i]) + kn - 65) % 26 + 65)

    elif text[i].islower():
        enc += chr((ord(text[i]) + kn - 97) % 26 + 97)

    elif text[i].isnumeric():
        enc += chr((ord(text[i]) + kn - 48) % 10 + 48)

print("Encryption Text: " + enc)
print('\n')

# Decryption Code
length_c = len(enc)
dec = ""

for k in range(0, 26):
    for i in range(length_c):
        if enc[i].isupper():
            dec += chr((ord(enc[i]) - k - 65) % 26 + 65)

        elif enc[i].islower():
            dec += chr((ord(enc[i]) - k - 97) % 26 + 97)

        elif enc[i].isnumeric():
            dec += chr((ord(enc[i]) - k - 48) % 10 + 48)

    print("Decryption Text: " + str(k) + ' '+ dec)
    dec = ''