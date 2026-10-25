
# FUNCTIONS IN SCRIPT: 

# encrypt(): this one encrypts a message by matching letters with words using the specified shift. 
# decrypt(): this decrypts messages using the specified shift.
# wordShiftFinder(): this finds words in the word_list.txt that match the specified letter and shift of letter.
# wordShiftFinderAuto(): this finds all letter shifts 1-5 and counts them, it does that for every letter of the alphabet.
# ceasar(): standard ceasar shift takes in text and shift amount and does a ceasar cipher can decrypt by making the original
# shift negative, example: text: "hello" shift: 5 >encrypt> mjqqt >decrypt> shift: -5 > hello.
# wordToOp(): turns a string in to valid operator commands that will be the same for that word

# what if you made the encrypt function take in a string and converted that into a shift pattern
# like say i did: "hi" as key that would be a 8-9 shift pattern h = 8 i = 9 but my shift only goes up to 5
# so i would have to circle back h = 1-2-3-4-5-1-2-3 (3) i = 1-2-3-4-5-1-2-3-4 (4) 
# i wonder if when you encoded a pattern like 1-2-1-2 then you did another pattern on top like 4-5-4-5 what would happen
# just tested it and the patterns do work they return to the original message
# ok i have a plan to integrate spark shift pattern per word i can have the format be like s12345 and that will set the shift 
# to that pattern it will work out perfect
# 
# the brute force decryptor should work by trying every pattern possible and giving the output but what is the most efficient
# way to do that first of all there is a 1/2 chance of it being either a spark or caesar shift operand
# then there is a 1/9 chance of the shift amount 
#
#
#


import random
from itertools import product

index = 0

with open("word_list.txt") as words:
    wordList = words.read().split()

def encrypt(text, shift, index):
    # make shift cycle through a list instead of having just one int
    
    shiftCycleList = list(shift)
    
    encryptedMessage = []
    encyrpt = text
    
    cryptList = encyrpt.split()

    

    retainSpaceList = []
    for word in cryptList:
        shred = list(word)
        retainSpaceList.append(shred)
    
    for lists in retainSpaceList:      
      encryptedMessage.append("/")

      for letters in lists:
        random.shuffle(wordList)
        cycle = int(shiftCycleList[index]) - 1

        for word in wordList:
            if word and len(word) >= cycle + 1 and word[cycle] == letters:
                encryptedMessage.append(word.lower())
                index = (index + 1) % len(shiftCycleList)
                
                break
    
    del encryptedMessage[0]
    
    print()

    output = ""

    for word in encryptedMessage:
        output += f"{word} "

    index = 0
    return output

def decrypt(text, shift, index):

    decryptList = text

    shiftCycleList = list(shift)

    wordList = decryptList.split()

    print()
    currentWord = 0
    output = ""
    for word in wordList:
       
        if word == "/" and wordList[currentWord + 1] == "/":
            output += " /"

        if word == "/":
            output += " "

        else:
            cycle = (int(shiftCycleList[index]) - 1) % len(word)
            output += word[cycle]

            index = (index + 1) % len(shiftCycleList)

        currentWord += 1
        
    index = 0
    return output
    

def caesar(text, shift, index):
    shiftCycleList = list(shift)

    cycle = int(shiftCycleList[index]) # -1 if want shift of 1 to equal same example: shift 1: a=a
    index = (index) % len(shiftCycleList)
    

    result = ""
    
    for char in text:
        if char.isalpha():
            cycle = int(shiftCycleList[index]) # -1
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + cycle) % 26 + base)
            index = (index + 1) % len(shiftCycleList)
        else:
            result += char

    index = 0
    return result

def caesarDecrypt(text, shift, index):
    shiftCycleList = list(shift)

    cycle = int(shiftCycleList[index]) # -1
    index = (index) % len(shiftCycleList)
    

    result = ""
    
    for char in text:
        if char.isalpha():
            cycle = int(shiftCycleList[index]) # -1
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + -cycle) % 26 + base)
            index = (index + 1) % len(shiftCycleList)
        else:
            result += char

    index = 0
    return result

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
    
    matchCounter = 0 
    x = int(shiftAmount)
    x -= 1

    for word in wordList:
        if len(word) > x:
            if word[x] == shiftLetter:
                matchCounter += 1
            
    print(f"There were ({matchCounter}) matches with ({shiftLetter}) with a ({shiftAmount}) letter shift")

def wordToOp(password):
    random.seed(password)
    sparkMax = 3 
    operandString = ""
    
    amountOfOperations = random.randint(2,6)

    while amountOfOperations > 0:

        operand = random.choice("cs")
        
        if operand == "c":
            shift = random.randint(1,25)
            operandString += f"{operand}{shift} "

            amountOfOperations -= 1

        elif operand == "s" and sparkMax > 0:
            shift = random.randint(1,5)
            operandString += f"{operand}{shift} "

            sparkMax -= 1
            amountOfOperations -= 1

    print(f"Operands used: {operandString}")
    return operandString

def bruteForcePatternCrack():
    stringsFound = ""
    text = input("What do you want to brute decrypt: ")
     
    # will goes up to a 6 number pattern example: c123456 might be possible operand
    # and will go up to 6 itterations example: c1 s1 c2 s2 c3 s3 might be possible key
    # it will also detect if a possible string is correct and put them in a list

    single_pairs = []

    choice = int(input("Amount of digits for operator for example, c1234 would be 4: "))
    choice2 = int(input("Amount of operators for example, c1 s1 c2 s2 would be 4: "))
    countLimit = int(input("How many word matches do you want at a minimum?\n"
    "(this is like a seive the higher the number the more word matches it will require): "))
    maxChar = int(input("What is the max amount of characters you want in your string?\n"
    "(do the closest number to what you think the final string has in letters): "))

    for op in ["c", "s"]:
        for shift_len in range(1, choice + 1):
            for digits in product("123456789", repeat=shift_len):
                single_pairs.append((op, "".join(digits)))

    for pair_count in range(1, choice2 + 1):
        for key in product(single_pairs, repeat=pair_count):
            #print(key)
            key1 = " ".join("".join(pair) for pair in key)

            patternList = key1.split()
            patternList.reverse()

            # c1 - 99 s 1 - 99 c1 c23 s123
            
            repeat = text

            for pattern1 in patternList:
                
                pattern1 = pattern1.lower()
                
                if pattern1[0] == "c":
                    shift = pattern1[1:]
                    caesar1 = caesarDecrypt(repeat, shift, index)
                    repeat = caesar1

                elif pattern1[0] == "s":
                    shift = pattern1[1:]
                    spark = decrypt(repeat, shift, index)
                    repeat = spark
            
            checkWords = repeat.split()
            counter = 0 
            for words in wordList:
                for word in checkWords:
                    if words == word and len(repeat) <= maxChar + 5:
                        counter += 1
                        
            print("Looking...")

            if counter >= countLimit:
                stringsFound += f"String found: {repeat}\n Operands: {key1}\n"
                  

    print(stringsFound)

