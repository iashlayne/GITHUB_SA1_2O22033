# EXERCISE 9 - INTEGER LIST

# Welcome the User
print("\n*-*-*-*-*-*-*-*-*-*-* Welcome to Integer List *-*-*-*-*-*-*-*-*-*-*\n\n")

# --Create an int list with 10 values--
# Assigned a variable "list_of_integers" with 10 integer values inside
list_of_integers = [5, 12, 21, 8, 32, 2, 18, 26, 19, 29]

# --Output the list using a for loop--
# Print the List of Integers
print("List of Integers:")
# using for loop to iterate each elements of list
for numbers in list_of_integers:
    # printing each numbers on same line with a space seperating each elements
    print(numbers,end=" ")
    
# print for next line
print('\n')

# --Output the highest and lowest value--

# Assigned a variable "highest_number" using max() function return to the highest value in iterable
highest_number = max(list_of_integers)
# Assigned a variable "lowest_number" using min() function return to the lowest value in iterable
lowest_number = min(list_of_integers)

# Print the assigned variable "highest_number" HIGHEST VALUE
print(f"The Highest Value in the List: {highest_number}")
# Print the assigned variable "lowest_number" LOWEST VALUE
print(f"The Lowest Value in the list: {lowest_number}\n")

# --Sort the elements in ascending order--

# Assigned a variable "ascending_order_list" using sorted() function returns to sorted list in iterable
ascending_order_list = sorted(list_of_integers)
# Print the assigned variable 'ascending_order_list' in "Ascending Order" 
print("Ascending Order:", ascending_order_list)


# --Sort the elements in descending order--

# Called the variable "list_of_integers" using .sort() function returns to sorted list in iterable
list_of_integers.sort()
# Called the variable "list_of_integers using .reverse() function to reverse and make
# it into descending order
list_of_integers.reverse()
ascending_order_list = sorted(list_of_integers)
# Print the assigned variable 'list_of_integers' in "Descending Order" 
print("Descending Order:", list_of_integers)

# --Append two elements--

# Called the variable "list_of_integers" using method .append() to add element
# in the list "list_of_integers"
list_of_integers.append(4)
list_of_integers.append(10)

# --Print the list after appending calling the variable "list_of_integers" 
# after we use the append() function--
print("\nThe list after appending:", list_of_integers)

# print for design purpose
print("\n\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")









