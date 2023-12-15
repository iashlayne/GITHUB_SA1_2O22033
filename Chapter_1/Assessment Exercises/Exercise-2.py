#EXERCISE 2 - MATHS

# Defining a function "check_valid_number" having a parameter (value) 
# to define the entered integer is valid
def check_valid_number(value):
    #It will return to remove the first ("-") negative integer if user input,
    # to check the remaining character if..
    # all are digits, if they are then "TRUE" otherwise, "FALSE"
    return value.replace("-","",1).isdigit()

#Intro to welcome user using math python machine
print("\n*-*-*-*HELLO, Welcome to MATH Python Machine*-*-*-*\n")


#We created a loop that if it is true and valid integer it will accept and break
# to continue to do the arithmetic operation
#Else the user input letter or any not number it will print ("Please enter a valid integer")
while True:
    #Assigned a variable "number_1" and func (input) for user to enter any number
    # Enter the first number that you want calculate 
    number_1_inpt = input("Enter your First Integer:")
    if check_valid_number(number_1_inpt):
        number_1 = int(number_1_inpt)
        break
    else:
        print("Please enter a valid integer.")
        
#Assigned a variable "number_2" and func (input) for user to enter any number
# Enter the second number that you want calculate 
while True:
    number_2_inpt = input("Enter your Second Integer:")
    if check_valid_number(number_2_inpt):
            number_2 = int(number_2_inpt)
            break
    else:
        print("Please enter a valid integer.")

#print for design purpose 
print("\n-----------------------------------------------")

# Assigned a varible "sum_output" to to make an adding operation (+)
# getting from the user input (number_1) and (number_2)
sum_output = number_1 + number_2
# Assigned a varible "difference_output" to to make a subtracting operation (-) 
# getting from the user input (number_1) and (number_2)
difference_output = number_1 - number_2
# Assigned a varible "difference_output" to to make a multiplying operation (*)
# getting from the user input (number_1) and (number_2)
product_output = number_1 * number_2

# We assigned if else condition
# If number_2 (second number) is not = 0 to check because zero division
# is undefined and can result error
if number_2 !=0:
    #If it second number is not equal to 0 then it will calculate the given numbers
    # from user input number_1 and number_2
    quotient_output = number_1 / number_2
else:
    #If the second number is 0 the quotient is set to 0 to prevent error while running the code
    quotient_output = 0

# ADDITION
# This will print the sum of the user input number_1 + number_2 and output : sum_output
print(f"The sum of {number_1} + {number_2}: {sum_output}\n")

# SUBTRACTION
# This will print the difference of the user input number_1 - number_2 and output : difference_output
print(f"The difference of {number_1} - {number_2}: {difference_output}\n")

# MULTIPLICATION
# This will print the product of the user input number_1 * number_2 and output : product_output
print(f"The product of {number_1} x {number_2}: {product_output}\n")

# DIVISION
# This will print the quotient of the user input number_1 / number_2 and output : difference_output
print(f"The quotient of {number_1} ÷ {number_2}: {quotient_output}")

#print for design purpose
print("-------------------------------------------------")