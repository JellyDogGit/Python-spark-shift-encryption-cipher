from spark_shift_functions import encrypt, decrypt, caesar, caesarDecrypt, wordShiftFinder, wordShiftFinderAuto, wordToOp, bruteForcePatternCrack

index = 0

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
If you want the brute force pattern cracker enter: 9
Exit enter: x

choose: """
        )
 #-------------------------------------------------------------------------               
    if choose == "1":

        text = input("Message to encrypt: ")
        shift = input("Shift amount (max 5) or pattern, example: 12345: ")

        print(encrypt(text, shift, index),"\n")
#-------------------------------------------------------------------------
    elif choose == "2":

        text = input("Message to decrypt: ")
        shift = input("Shift amount (max 5) or pattern, example: 12345: ")
        
        print(decrypt(text, shift, index),"\n")
#-------------------------------------------------------------------------
    elif choose == "3":
        wordShiftFinder()
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------
    elif choose == "5":
        text = input("Message to encrypt: ")
        ceasarStr = input("Shift amount for ceasar: ")
        shift = input("Shift amount for spark shift (max 5): ")
        encryptedCeasar = caesar(text, ceasarStr, index)

        print(encrypt(encryptedCeasar, shift, index),"\n")
#-------------------------------------------------------------------------
    elif choose == "6":
        choice = input("Do you want to encrypt or decrypt caesar: 1 for encrypt 2 for decrypt: ")
        if choice == "1":
            text = input("Message to encrypt: ")
            ceasarStr = input("Shift amount for ceasar you can choose pattern, example: 12345: ")
            
            print(caesar(text, ceasarStr, index))
        elif choice == "2":
            text = input("Message to decrypt: ")
            ceasarStr = input("Shift amount for ceasar you can choose pattern, example: 12345: ")
                
            print(caesarDecrypt(text, ceasarStr, index),"\n")

#-------------------------------------------------------------------------

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
you can also patterns within each iteration example: c123 s123 c4523 s2341 c2141 s3523 (this is impossible to decode by hand)


The letter defines what method and the number defines the shift amount,
so for the examle that would be a Caesar shift by 1 then Spark shift by 1 and so on

enter pattern here: """)

            patternList = pattern.split()

            

            for pattern1 in patternList:
                
                
                pattern1 = pattern1.lower()
                
                if pattern1[0] == "c":
                    shift = pattern1[1:]
                    caesar1 = caesar(text, shift, index)
                    text = caesar1

                    #print(f"caesar({pattern1[1]})")

                elif pattern1[0] == "s":
                    shift = pattern1[1:]
                    spark = encrypt(text, shift, index)
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
                    cycle = encrypt(text, shift, index)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")

            elif choice == "n": 
                
                shift = input("Shift amount for spark shift (max 5): ")
                amountOfSparkShift = int(input("How many times do you want to do spark shift: "))

                while amountOfSparkShift > 0:
                    cycle = encrypt(text, shift, index)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")
#-------------------------------------------------------------------------
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

here an example format: c1 s1 c2 s2 c3 s3 (capitalization does not matter)
you can also patterns within each iteration example: c123 s123 c4523 s2341 c2141 s3523 (this is impossible to decode by hand)

The letter defines what method and the number defines the shift amount,
so for the examle that would be a Caesar decrypt shift by 1 then Spark decrypt shift by 1 and so on

enter pattern here: """)

            patternList = pattern.split()
            patternList.reverse()

            for pattern1 in patternList:
                
                pattern1 = pattern1.lower()
                
                if pattern1[0] == "c":
                    shift = pattern1[1:]
                    caesar1 = caesarDecrypt(text, shift, index)
                    text = caesar1

                elif pattern1[0] == "s":
                    shift = pattern1[1:]
                    spark = decrypt(text, shift, index)
                    text = spark
                    
            print(text)

        elif choice1 == "n":
            
            
            text = input("Message to decrypt: ")
            shift = input("Shift amount for spark shift (max 5): ")
            amountOfSparkShift = int(input("How many cycles of decryption: "))

            choice = input("Do you want to decrypt with caesar also? (y/n): ")
            
            if choice == "y":
                caesarShiftAmount = int(input("Shift amount for caesar shift: "))
                while amountOfSparkShift > 0:
                    cycle = decrypt(text, shift, index)
                    text = cycle
                    amountOfSparkShift -= 1
                print(caesar(text, -caesarShiftAmount),"\n")

            elif choice == "n":

                while amountOfSparkShift > 0:
                    cycle = decrypt(text, shift, index)
                    text = cycle
                    amountOfSparkShift -= 1
                print(text,"\n")
                
    elif choose == "9":
        bruteForcePatternCrack()
       
    elif choose == "x":
        print("Goodbye!")
        break