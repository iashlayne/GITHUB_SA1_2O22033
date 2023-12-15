#EXERCISE 11 - YEAR TUPLES

# WELCOME THE USER
print("\n*-*-*-*-*-*-*-*-*-*-* Welcome to YEAR TUPLES *-*-*-*-*-*-*-*-*-*-*\n\n")
# Assigned a variable "list_of_years" defined the sequence of year 
list_of_years = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Print the third-of-last value from the tuple "list_of_years" using -3 to indicides...
# counting the position from the last/end of sequence
print("The value at index -3:", list_of_years[-3], "\n")

# Printing the Original Tuple "list_of_years"
print("The Original Tuple:", list_of_years, "\n")
# Printing the Reversed Tuple "list_of_years" using the class() reversed
print("The Reversed Tuple:", tuple(reversed(list_of_years)), "\n")

# Printing the tuple's count of year "2009" calling the variable "list_of_years" using 
# method() count to how many times in the tuples has been listed (2009)
print("The tuple's count for the year 2009: ", list_of_years.count(2009), "\n")

# Printing the Index value of "2018" calling the variable "list_of_years" using
# index method () to check the index value starting from 0
print("Index Value of 2018:", list_of_years.index(2018), "\n")

# Printing the "Length of the given tuple" using len () or length function 
# to check the number of items in the tuple container
print("Length of the given tuple:", len(list_of_years), "\n")

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n\n")