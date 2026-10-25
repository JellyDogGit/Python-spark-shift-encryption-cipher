import random

with open("word_list.txt") as words:
    wordList = words.read().split()
#print(len(wordList))

encryptMultiMessage = ""
decryptMultiMessage = ""


def encrypt():

    shift = 2
    encryptedMessage = []
    encyrpt = input("Word to encrypt: ")
    
    cryptList = encyrpt.split()

    retainSpaceList = []
    for word in cryptList:
        shred = list(word)
        retainSpaceList.append(shred)
    
    for lists in retainSpaceList:
      encryptedMessage.append("/")
      for letters in lists:
        random.shuffle(wordList)
        for word in wordList:
            if word and len(word) >= shift and word[1] == letters:
                encryptedMessage.append(word.lower())
                break

    del encryptedMessage[0]

    print("\n\n\n")
    for word in encryptedMessage:
        print(word, end=" ")




# the message loses too much information for multipul encryptions because of all the different words being used
def encryptMulti(message):
    global encryptMultiMessage

    shift = 2
    encryptedMessage = []
    encyrpt = message
    
    cryptList = encyrpt.split()

    retainSpaceList = []
    for word in cryptList:
        shred = list(word)
        retainSpaceList.append(shred)
        #for word in retainSpaceList:
            
            #list(word)
            
    #print(retainSpaceList)
    
    
    
    for lists in retainSpaceList:
      encryptedMessage.append("/")
      for letters in lists:
        random.shuffle(wordList)
        for word in wordList:
            if word and len(word) >= shift and word[1] == letters:
                encryptedMessage.append(word)
                break
    encryptMultiMessage = " ".join(encryptedMessage)
    for word in encryptedMessage:
        print(word, end=" ")




    
def decrypt():
    decryptList = input("Word to decrypt: ")
    shift = 2
    wordList = decryptList.split()

    print("\n\n\n")
    currentWord = 0
    for word in wordList:
            
            #if len(word) >= shift and word[1] == True:
            if word == "/" and wordList[currentWord + 1] == "/":
                # del wordList[currentWord + 1]
                print(" /", end="")
            if word == "/":
                print(end=" ")

            else:
                print(word[1], end="")

            currentWord += 1

    

def decryptMulti(message):
    global decryptMultiMessage
    decryptList = message
    shift = 2
    wordList = decryptList.split()

    print("\n\n\n")
    for word in wordList:
        #if len(word) >= shift and word[1] == True:
        if word == "/":
            
            print(end=" ")
            decryptMultiMessage = " ".join(wordList)
            print(f"decrypt global var /// {decryptMultiMessage}")

        else:
            print(word[1], end="")
            decryptMultiMessage = "".join(wordList)

            print(f"decrypt global var {decryptMultiMessage}")

def wordShiftFinder():

    shiftAmount = input("What shift amount do you want to look for: ")
    shiftLetter = input("What letter do you want to find in that shift amount: ")

    matchCounter = 0 

    x = int(shiftAmount)
    x -= 1

    for word in wordList:
        if len(word) > x:
            if word[x] == shiftLetter:
                matchCounter += 1
                print(word)
               
    print(f"amount found: {matchCounter}")

def wordShiftFinderAuto(shiftAmount, shiftLetter):

    # shiftAmount = input("What shift amount do you want to look for: ")
    # shiftLetter = input("What letter do you want to find in that shift amount: ")

    matchCounter = 0 
    x = int(shiftAmount)
    x -= 1

    for word in wordList:
        if len(word) > x:
            if word[x] == shiftLetter:
                matchCounter += 1
            
            

    print(f"There were ({matchCounter}) matches with ({shiftLetter}) with a ({shiftAmount}) letter shift")
choose = input("Encrypt: press 1, Decrypt: press 2, Find shift letters: press 3, Look through all shifts with every letter: press 4\n\n\n")
               



if choose == "1":
    encrypt()


elif choose == "2":
    decrypt()

elif choose == "3":
    wordShiftFinder()

elif choose == "4":
    letters = "abcdefghijklmnopqrstuvwxyz"
    letterList = list(letters)
    
    for letter in letterList:
        # this will test all shift for every letter
        wordShiftFinderAuto(1, letter)
        wordShiftFinderAuto(2, letter)
        wordShiftFinderAuto(3, letter)
        wordShiftFinderAuto(4, letter)
        wordShiftFinderAuto(5, letter)
# elif choose == "3":
#     inputMessage = input("Word to encrypt: ")
#     inputAmmount = input("How many times do you want to encrypt: ")

#     ammount = int(inputAmmount)

#     while ammount > 0:
#         encryptMulti(inputMessage)
#         inputMessage = encryptMultiMessage
#         ammount -= 1
#         print("\n\n\n")


# elif choose == "4":
#     inputMessage = input("Word to decrypt: ")
#     inputAmmount = input("How many times do you want to decrypt: ")
    
#     ammount = int(inputAmmount)
    
#     while ammount > 0:
#         decryptMulti(inputMessage)
#         inputMessage = decryptMultiMessage
#         print("\n\n\n")
#         ammount -= 1

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


import random


def wordToOp(password):
    random.seed(password)
    sparkMax = 3 
    operandString = ""

    #endOnCaesar = input("Do you want to prevent the pattern from ending on a caesar shift? (y/n): ")
    
    amountOfOperations = random.randint(2,6)

    print(amountOfOperations)

    while amountOfOperations > 0:

        operand = random.choice("cs")
        

        if operand == "c":
            shift = random.randint(1,25)
            operandString += f"{operand}{shift} "
            #print(f"{operand}{shift}")

            amountOfOperations -= 1

        elif operand == "s" and sparkMax > 0:
            shift = random.randint(1,5)
            operandString += f"{operand}{shift} "
            #print(f"{operand}{shift}")

            sparkMax -= 1
            amountOfOperations -= 1

    # if endOnCaesar == "y":
    #     while True:
    #         if operandString[-2] == "c":
    #             operandString = operandString[:-3]
                           
    #         elif operandString[-2] == "s":
    #             return operandString
    #         break
        
    # elif endOnCaesar == "n":
    #     #print(operandString)
    return operandString
        
    # letters1 = list(password)
    # print(letters1)



password = input("What word would you like to into operands?: ")
# password = input("What word would you like to into operands?: ")
print(wordToOp(password))

# MAIN.PY CODE -----------------------------------------------------------

from spark_shift_functions import encrypt, decrypt, caesar, wordShiftFinder, wordShiftFinderAuto, wordToOp


while True:
    choose = input("""

Encrypt with spark shift: enter 1
Decrypt with spark shift: enter 2
Find spark shift letters (de-bug): enter 3
Look through all spark shifts with every letter (de-bug): enter 4 
To do ceasar + spark shift enter: 5 
If you want to encrypt or decrypt with caeser enter: 6
If you want your message to be impossible to crack enter: 7
If you want the master decrypter enter: 8
Exit enter: 9

choose: """
        )
                
    if choose == "1":

        text = input("Message to encrypt: ")
        shift = input("Shift amount (max 5): ")

        print(encrypt(text, shift),"\n")

    elif choose == "2":

        text = input("Message to decrypt: ")
        shift = input("Shift amount (max 5): ")
        
        print(decrypt(text, shift),"\n")

    elif choose == "3":
        wordShiftFinder()

    elif choose == "4":
        letters = "abcdefghijklmnopqrstuvwxyz"
        letterList = list(letters)

        for letter in letterList:
            # this will test all shift for every letter
            wordShiftFinderAuto(1, letter)
            wordShiftFinderAuto(2, letter)
            wordShiftFinderAuto(3, letter)
            wordShiftFinderAuto(4, letter)
            wordShiftFinderAuto(5, letter)

    elif choose == "5":
        text = input("Message to encrypt: ")
        ceasarStr = input("Shift amount for ceasar: ")
        shift = input("Shift amount for spark shift (max 5): ")
        encryptedCeasar = caesar(text, ceasarStr)

        print(encrypt(encryptedCeasar, shift),"\n")

    elif choose == "6":
        choice = input("Do you want to encrypt or decrypt caesar: 1 for encrypt 2 for decrypt: ")
        if choice == "1":
            text = input("Message to encrypt: ")
            ceasarStr = input("Shift amount for ceasar: ")
            
            print(caesar(text, ceasarStr))
        elif choice == "2":
            text = input("Message to decrypt: ")
            ceasarStr = int(input("Shift amount for ceasar: "))
                
            print(caesar(text, -ceasarStr),"\n")

    elif choose == "7":
        choice1 = input("Do you want to encrypt with a pattern? (y/n): ")

        if choice1 == "y":
            text = input("Message to encrypt: ")
            useKey = input("Do you want to use a key string to encrypt? (y/n): ")
            if useKey == "y":
                passStr = input("What string do you want to encrypt your message with?: ")
                pattern = wordToOp(passStr)
            elif useKey == "n":

                pattern = input("""

Please define your pattern.

here an example format: C1 S1 C2 S2 C3 S3 (capitalization does not matter)

The letter defines what method and the number defines the shift amount,
so for the examle that would be a Caesar shift by 1 then Spark shift by 1 and so on

enter pattern here: """)

            patternList = pattern.split()
            

            for pattern1 in patternList:
                shift = int(pattern1[1])
                pattern1 = pattern1.lower()
                
                if pattern1[0] == "c":
                    caesar1 = caesar(text, shift)
                    text = caesar1

                    #print(f"caesar({pattern1[1]})")

                elif pattern1[0] == "s":
                    spark = encrypt(text, shift)
                    text = spark
                    #print(f"spark({pattern1[1]})")
            print(text)

        
        elif choice1 == "n":
            text = input("Message to encrypt: ")
            choice = input("Do you want to double encrypt with caesar and spark shift? (y/n): ")
            
            if choice == "y":
                
                ceasarStr = input("Shift amount for ceasar: ")
                shift = input("Shift amount for spark shift (max 5): ")
                amountOfSparkShift = int(input("How many times do you want to do spark shift: "))

                encryptedCeasar = caesar(text, ceasarStr)

                text = encryptedCeasar

                while amountOfSparkShift > 0:
                    cycle = encrypt(text, shift)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")

            elif choice == "n": 
                
                shift = input("Shift amount for spark shift (max 5): ")
                amountOfSparkShift = int(input("How many times do you want to do spark shift: "))

                while amountOfSparkShift > 0:
                    cycle = encrypt(text, shift)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")

    elif choose == "8":
        choice1 = input("Do you want to decrypt a pattern? (y/n): ")
        if choice1 == "y":
            text = input("Message to decrypt: ")
            useKey = input("Do you want to use a key string to decrypt? (y/n): ")

            if useKey == "y":
                passStr = input("What string do you want to decrypt your message with?: ")
                pattern = wordToOp(passStr)
                
            elif useKey == "n":
                pattern = input("""

Please define your pattern.

here an example format: C1 S1 C2 S2 C3 S3 (capitalization does not matter)

The letter defines what method and the number defines the shift amount,
so for the examle that would be a Caesar decrypt shift by 1 then Spark decrypt shift by 1 and so on

enter pattern here: """)

            patternList = pattern.split()
            patternList.reverse()

            for pattern1 in patternList:
                shift = int(pattern1[1])
                pattern1 = pattern1.lower()
                
                if pattern1[0] == "c":
                    caesar1 = caesar(text, -shift)
                    text = caesar1

                    #print(f"caesar({pattern1[1]})")

                elif pattern1[0] == "s":
                    spark = decrypt(text, shift)
                    text = spark
                    #print(f"spark({pattern1[1]})")
            print(text)

        elif choice1 == "n":
            
            
            text = input("Message to decrypt: ")
            shift = input("Shift amount for spark shift (max 5): ")
            amountOfSparkShift = int(input("How many cycles of decryption: "))

            choice = input("Do you want to decrypt with caesar also? (y/n): ")
            
            if choice == "y":
                caesarShiftAmount = int(input("Shift amount for caesar shift: "))
                while amountOfSparkShift > 0:
                    cycle = decrypt(text, shift)
                    text = cycle
                    amountOfSparkShift -= 1
                print(caesar(text, -caesarShiftAmount),"\n")

            elif choice == "n":

                while amountOfSparkShift > 0:
                    cycle = decrypt(text, shift)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")
    elif choose == "9":
        print("Goodbye!")
        break