print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* MATH CALCULATOR -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# import module operator
import operator

# define func() addition
def addition(x, y):
    # Operator.add + to add x and y
    return operator.add(x, y)

# define func() subtraction
def subtraction(x, y):
    # Operator.sub - to minus x and y
    return operator.sub(x, y)
 
# define func() multiplication
def multiplication(x, y):
    # Operator.mul * to multiply x and y
    return operator.mul(x, y)

# define func() division
def division(x, y):
    # this is error 0
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Error: Division by zero"
    
# define func() modulus
def modulus(x, y):
    
     # Operator.mod * to module x and y
    return operator.mod(x, y)

# define func() check_greater
def check_greater(x, y):
    # Check great value
    return max(x, y)

# define func calculator_selection()
def calculator_selection():
    # print math operation selection
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")

# called func calculator_selection()
calculator_selection()

# This is for quit option 
while True:
    option = input("Enter option (1-6) or Q to quit: ").upper()
    
    # it will break if Q key is pressed
    if option == 'Q':
        break

    # If option 1-6 chose it will show Enter first number: Enter second number: - user input
    if option.isdigit() and 1 <= int(option) <= 6:
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        # ERROR
        except ValueError:
            print("Invalid input. Please enter valid integer.")
            continue
        
        #IF ELIF ELSE CONDITION
        if option == '1':
            result = addition(number1, number2)
        elif option == '2':
            result = subtraction(number1, number2)
        elif option == '3':
            result = multiplication(number1, number2)
        elif option == '4':
            result = division(number1, number2)
        elif option == '5':
            result = modulus(number1, number2)
        elif option == '6':
            result = check_greater(number1, number2)
            
        # print ouput {result}
        print(f"Output: {result}\n")
    # Else (try again invalid choice or press q to quit)
    else:
        print("Invalid choice. Please enter a digit from 1 to 6 or your choice Q to quit.\n")
        
# print calculator now is closed
print("Calculator is now closed.")