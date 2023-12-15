# Exercise 3 - Reading to a list

# import module random
import random

# Generate a list of 100 random integers
rand_number = [random.randint(1, 1000) for _ in range(100)]

# Print word ""List of Random Integers:")"
print("\n\nList of Random Integers:\n")
# print the random numbers that has been picked
print(rand_number)

# This is where it convert the list items into numbers/integer 
num_values = [int(num) for num in rand_number]
print("\nThe List Values of Elements as Integers:")
# Print the num values in random choice
print(num_values)