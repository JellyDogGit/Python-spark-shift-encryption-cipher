
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