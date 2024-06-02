#Functions with Inputs and Caeser Cipher


def caesar(text, shift, direction):
        encoding = True
        if direction == "decode":
            shift *= -1
        new_text = ""
        for letter in text:
            if letter.isalpha():
                new_text += chr((ord(letter) - 97 + shift) % 26 + 97)
            else:
                new_text += letter

        print(new_text)

encoding = True
while encoding:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    direction = input()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    end = input("Would you like to go again? Type 'yes' or 'no':\n").lower()
    if end == "no":
        encoding = False
        print("Goodbye")
