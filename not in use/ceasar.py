def caesar(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

choose = input("Encrypt or decrypt ceasar? 1 for encrypt, 2 for decrypt")

if choose == "1":

    text = input("What text do you want to ceasarfy: ")
    shift = int(input("How many shift do you want?"))
    print(caesar(text, shift))
if choose == "2":
    text = input("What text do you want to unceasarfy: ")
    shift = int(input("How many shift do you want to go back?"))

    print(caesar(text, -shift))
