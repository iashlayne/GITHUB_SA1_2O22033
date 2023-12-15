# EXERCISE 7 - EVEN NUMBERS 

# Print intro "EVEN NUMBERS" to welcome user "1-100"
print("\n*-*-*-*-*-*-* EVEN NUMBERS *-*-*-*-*-*-*")
print("                1 - 100                  \n")

# Define a function 'even_numbers_only'
def even_numbers_only():
    # assigned a variable "number" and its value 1 where it will starts from 1
    number = 1
    # while loop continues "number" less than or equals than 100
    while number <= 100:
        # This is to check if the number is odd 
        if number % 2 != 0:
            # to increase integers from 1 (integers) - odd numbers
            number += 1
            # Skip the odd numbers
            continue
        # Print even numbers
        print(number)
        # to increase integers from 1 (integers) - even numbers
        number += 1


# if __name__ is a variable in python where script is executed
# __name__ set to __main__ if function (even_numbers_only) the program being run 
if __name__ == "__main__":
    even_numbers_only()
