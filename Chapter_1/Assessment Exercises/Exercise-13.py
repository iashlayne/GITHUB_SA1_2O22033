#EXERCISE 13 - PRODUCT OF LIST ITEMS

# Welcome the user
print("\n*-*-*-*-*-*-*-*-*-*-* Welcome to PRODUCT OF LIST ITEMS *-*-*-*-*-*-*-*-*-*-*\n")
# Defined a function() product_of_list_items to calculate the product of list items
def product_of_list_items(items_list):
    # We started with product value of 1
    product = 1
    # We multiply for each value in items_list
    for value in items_list:
        # the product times equals the value 
        product *= value
    # Returning the final product which is back to the main program
    return product

# Assigned a variable "the_list" consisting of different values
the_list = [14, 23, 35, 8, 6, 12, 78, 42, 5, 20]

# Assigned a variable "product_output" called the function we made earlier and 
# called the variable "the list" with list of integers to get the product
product_output = product_of_list_items(the_list)

# Printing the Product of the values from the list called the variable "product_output"
# to print the outcome 
print("Here's the product of List Values:", product_output)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")


