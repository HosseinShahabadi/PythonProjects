import os
from images import logo
os.system('cls' if os.name == 'nt' else 'clear')

'''
This Python script implements a modified version of the classical Caesar Cipher,
a simple substitution cipher technique. Unlike the traditional Caesar Cipher
which shifts each letter in the plaintext by a fixed number of positions in the alphabet,
this modified version introduces additional complexity through customizable shifting rules.
The script includes advanced security measures such as the option to comment out number
encoding and decoding sections for heightened security.
These sections can be uncommented and utilized if deemed necessary, but they are disabled by default.
'''

# Encryption based on "Caesar Cipher"
def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text.append(alphabet[(index + shift) % len(alphabet)])
        elif char in symbols:
            index = symbols.index(char)
            encrypted_text.append(symbols[(index + shift + 2) % len(symbols)])
        # elif letter in numbers:
        #     index = numbers.index(letter)
        #     encrypted_text.append(numbers[(index + shift + 5) % len(numbers)])
        else:
            encrypted_text.append(char)
    print(f"Your encoded message: {"".join(encrypted_text)}")

# Decryption based on "Caesar Cipher"
def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_text.append(alphabet[(index - shift) % len(alphabet)])
        elif char in symbols:
            index = symbols.index(char)
            decrypted_text.append(symbols[(index - shift - 2) % len(symbols)])
        # elif letter in numbers:
        #     index = numbers.index(letter)
        #     decrypted_text.append(numbers[(index - shift - 5) % len(numbers)])
        else:
            decrypted_text.append(char)
    print(f"Your decoded message: {"".join(decrypted_text)}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '/', '?', '`', '~']

print(logo)
while 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: "))
        encrypt(text, shift)
        break
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: "))
        decrypt(text, shift)
        break
    else:
        print("Wrong input, please try again")
