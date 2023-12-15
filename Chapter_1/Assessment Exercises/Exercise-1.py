# EXERCISE 1 -  User Input Output

# Assigned a variable "user_name" where user can input their name, using "input" function. 
# using method to make the first letter uppercased ".title"
user_name = input("'\nHello, user! What is your name?").title()
#Assigned a variable "user_age" where user can input their age in "int" class and input function.
user_age = int(input("What is your age?"))

# Using print function to print meeting the "name of the user" where we called using curly brackets
print(f"It is good to meet you, {user_name} S")

# Assigned a varable "length_user" where it will calculate the length of user's name using "len" function.
length_user = len(user_name)
# Assigned a variable to add + 1 for his present age to calculate for his age in a year
user_age_next_year = user_age + 1

# Print the length of the name calling the variable we made "length_user" that has been calculated the length of user's name
print(f"The length of your name is: {length_user}")
#Print the user's age next year calling the variable "user_age_next_year has been calculated the current age + 1"
print(f"You will be {user_age_next_year} in a year.")

# OUTPUT:
#Hello, user!
#What is your name?
#alpha
#What is your age?
#22
#It is good to meet you, Alpha S
#The length of your name is:
#5
#You will be 23 in a year.

