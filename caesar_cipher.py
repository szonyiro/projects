from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


# v1 individual functions
# def encrypt(plain_text, shift_amount):
#     encrypted = ""
#     for letter in plain_text:
#         encrypted += alphabet[alphabet.index(letter) + shift]
#     print(f"\nThe coded text is {encrypted}")
#     return
#
#
# def decrypt(plain_text, shift_amount):
#     decrypted = ""
#     for letter in plain_text:
#         decrypted += alphabet[alphabet.index(letter) - shift]
#     return print(f"\nThe decoded text is {decrypted}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)


# v2 two functions combined into one
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if direction == "encode":
#         for char in start_text:
#             if char in alphabet:
#                 end_text += alphabet[alphabet.index(char) + shift]
#             else:
#                 end_text += char
#     elif direction == "decode":
#         for char in start_text:
#             if char in alphabet:
#                 end_text += alphabet[alphabet.index(char) - shift]
#             else:
#                 end_text += char
#
#     print(f"\nThe {cipher_direction}d text is {end_text}")

# v3 cleaning the function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""  # empty variable
    for char in start_text:  # loop for checking characters in text from input
        if char in alphabet:  # if character is in alphabet
            if direction == "encode":  # if encode/decode, shifts the alphabet by the inputted shift number
                end_text += alphabet[alphabet.index(char) + shift]
            elif direction == "decode":
                end_text += alphabet[alphabet.index(char) - shift]
        else:  # if character is not in alphabet, added to the variable without change
            end_text += char
    print(f"\nThe {cipher_direction}d text is {end_text}")  # prints out encoded/decoded text


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    repeat = input("\nType 'yes' to go again. Otherwise type 'exit'.")
    clear()
    if repeat == "exit":
        print("Good bye!")
        break




