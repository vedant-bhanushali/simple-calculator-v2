print("Welcome to AOS vedant's calculator v2 ")
print("                                   ")
print("See the option and select the number when asked")
print("                                   ")
print("Multiply : 1")
print("Divide : 2")
print("Add : 3")
print("Subtract : 4 ")
print("power : 5")

print("                                   ")

choose = (input("choose the option from above (1,2,3,4,5) :  "))
print("                                   ")
print ("made by aos vedant")
print("                                   ")
print("select the numbers of your operation")
print("                                   ")
num1 = int(input("number 1 :   "))
num2 = int(input("number 2 :   "))
print("                                   ")

ques1 = (input(" Do you want to do one more time digit in the operation ?  , y/n ( USE ONLY LOWERCASE): "))

print("                                   ")

if( ques1 == "y" ) :
    print("choose your 3rd number :   ")

elif( ques1 == "n") :
    print(" Loading furthur , ignore and input any number at the place of number 3")
print("                                   ")
num3 = int(input("number 3 :   "))
print("                                   ")
if( ques1 == "y" and choose == "1") :
    print(" THE ANSWER FOR NUMBER 3 DIGIT MULTIPLICATION =  " , num1 * num2 * num3 )

elif( ques1 == "y" and choose == "2") :
    print(" THE ANSWER FOR NUMBER 3 DIGIT DIVISION =  " , num1 / num2 / num3 )

elif( ques1 == "y" and choose == "3") :
    print(" THE ANSWER FOR NUMBER 3 DIGIT ADDITION =  " , num1 + num2 + num3 )

elif( ques1 == "y" and choose == "4") :
    print(" THE ANSWER FOR NUMBER 3 DIGIT SUBTRACTION =  " , num1 - num2 - num3 )

elif( ques1 == "y" and choose == "5") :
    print(" THE ANSWER FOR NUMBER 3 DIGIT POWER =  " , num1 ** num2 ** num3 )

# 3 digit operation ^ upwards & 2 digit operation downwards
# Made by aos vedant

elif( choose == "1") :
    print("THE ANSWER  FOR NUMBER 2 DIGIT MULTIPLICATION = " , num1 * num2)



elif( choose == "2"):
    print("THE ANSWER  FOR NUMBER 2 DIGIT DIVISION =  " , num1 / num2)



elif( choose == "3"):
    print("THE ANSWER  FOR NUMBER 2 DIGIT ADDITION =  " , num1 + num2)



elif( choose == "4"):
    print("THE ANSWER  FOR NUMBER 2 DIGIT SUBTRACTION =  " , num1 - num2)

elif( choose == "5") :
    print("THE ANSWER  FOR NUMBER 2 DIGIT  POWER =  " , num1 ** num2)

else :
    print("wrong option choosen which was given at the start , TRY AGAIN")
print("                                   ")

print (" Thank you for using aos calculator")
print ("  Made by aos vedant")
