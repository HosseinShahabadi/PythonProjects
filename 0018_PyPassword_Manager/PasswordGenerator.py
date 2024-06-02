import random

class PasswordGenerator:
    def generatePassword():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        no_letters = random.randint(8, 10)
        no_symbols = random.randint(2, 4)
        no_numbers = random.randint(2, 4)

        # Generating password (in Sequence)
        userpassword = []
        for char in range(1, no_letters + 1):
            userpassword += letters[random.randint(0, len(letters) - 1)]
        for char in range(1, no_symbols + 1):
            userpassword += symbols[random.randint(0, len(symbols) - 1)]
        for char in range(1, no_numbers + 1):
            # We can also use random.choice()
            userpassword += random.choice(numbers)

        # Shuffle the output (for more Security)
        random.shuffle(userpassword)

        return ''.join(userpassword)
