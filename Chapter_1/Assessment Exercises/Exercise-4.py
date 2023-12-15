# EXERCISE 4 : LARGEST NUMBER

# Defined a func "get_highest_number" to if elif else condition from number_1, number_2, number_3
def get_highest_number(number_1, number_2, number_3):
    # If #1 is greater than or equals than #2 and #1 is greater than or equals than #3 
    # It will return #1 which is the highest
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    # If #2 is greater than or equals than #1 and #2 is greater than or equals than #3 
    # It will return #2 which is the highest
    elif number_2 >= number_1 and number_2 >= number_3:
        return number_2
    # Else #3 is greater than or equals than #1 and #3 is greater than or equals than #1
    # It will return #3 which is the highest
    else:
        return number_3

# Defined a function main
def main():
    
    # Print to welcome the user
    print("\n*-*-*-PYTHON MACHINE - FIND THE HIGHEST NUMBER-*-*-*\n")
    
    #Input the number_1, number_2, and number_3 - using float where user can 
    # input decimal numbers/integers 
    number_1 = float(input("Input your 1st number:"))
    number_2 = float(input("Input your 2nd number:"))
    number_3 = float(input("Input your 3rd number:"))
    
    # Assigned a variable "highest_number" called the func (get_highest_number)
    # to find the highest number
    # based from the user input number_1, number_2, number_3
    highest_number = get_highest_number(number_1, number_2, number_3)
    
    # Print the highest number from the variable "highest_number"
    print(f"\nThe HIGHEST NUMBER : {highest_number}")
    
    # Print "Thank You, Have a nice day!"
    print("*-*-*-*-*-* THANK YOU, HAVE A NICE DAY! *-*-*-*-*-* ")

# if __name__ is a variable in python where script is executed
# __name__ set to __main__ if function (main) the program being run
if __name__ == "__main__":
    main()
    
    