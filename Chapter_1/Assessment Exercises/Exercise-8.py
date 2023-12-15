# EXERCISE 8 - PRINT PATTERN

# Defined a variable 'number_pattern' with a parameter 'line'
def number_pattern(line):
    # This is OUTER loop iterates over the line it starting from 1 to line
    # This represents new row in each line
    for n in range(1, line + 1):
        # This is INNER loop iterates over the line it starting from 1 to current line number (o) 
        # This represents the numbers in each row
        for o in range (1,n + 1):
            # It will keep the numbers on same line
            # Each number in the inner loop, it will print the numbers followed by a space (end=" ")
            print(o, end=" ")
        # After every numbers in row are printed, this will print empty line moving next line
        # for next row
        print()

# if __name__ is a variable in python where script is executed
# this function "number_pattern(5)" print the number of rows you want to be displayed as pattern
# It will display 5 ROWS
if __name__ == "__main__":
    number_pattern(5)
    
    
    
    