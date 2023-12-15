# EXERCISE 6 - FIZZBUZZ

print("\n*-*-*-*-*-*-*-* BIZZ FUZZ *-*-*-*-*-*-*-*\n")
# Defined a function 'bizz_fuzz'
def bizz_fuzz():
    
    # Using loop with range (), for loop iterating number 1-100 using range(1,101)
    for number in range(1, 101):
        
        # assigned a variable "result" 
        # (number % 3 == 0) * Fizz checks if the number is divisble (%) by 3 produce string "Fizz",
        # or else an empty string 
        # (number % 5 == 0) * Buzz checks if the number is divisble (%) by 5 produce string "Buzz", 
        # or else an empty string 
        # "Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0)...
        # If both numbers are divisible by 3 and 5 concatenating the FizzBuzz strings...
        # or empty strings (original number from range) if not
        result = "Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0)
        
        # print the 'result' which was in literal string "Fizz", "Buzz" or "FizzBuzz" 
        # print 'number' - an integer when its not divisible to numbers 3 and 5
        print(result or number)

# if __name__ is a variable in python where script is executed
# __name__ set to __main__ if function (bizz_fuzz) the program being run 
if __name__ == "__main__":
    bizz_fuzz()
    