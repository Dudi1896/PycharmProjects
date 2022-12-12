# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #7
# Author: Denzel Udemba
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.

def morse_encryption():
    stored_input = input('Please enter your text to be encrypted: ')

    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                  '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                  '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    # char placeholder
    cipher = ''

    # Automatically convert all input to uppercase to match morse dict
    caped_input=stored_input.upper()

    # parse through each char in the stored input that the user put in
    # then match the K:V pair from the char and add it to the cipher
    for char in caped_input:
        if char != ' ':
            cipher += morse_dict[char] + ' '
        else:
            cipher += ' '

    print(cipher)


def main():
    while True:
        try:
            morse_encryption()
        except:
            break


if __name__ == "__main__":
    main()
