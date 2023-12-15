# Exercise 1 - Basic Math

import math
print("\n-*-*-*-*-*-*-*CEIL, FLOOR, FACTORIAL, SQUARE ROOT-*-*-*-*-*-*-*\n")
# CEIL
# Assigned variable a_ceil = 2.3 float (decimal)
a_ceil = 2.3
# Assigned variable ceil_output and use math to calculate ceil calling variable a_ceil
ceil_output = math.ceil(a_ceil)
# Print the a_ceil and ceil_output value
print(f"For a = {a_ceil}, ceil of a is: {ceil_output}")

# FLOOR
# Assigned variable a_floor = 2.3 float (decimal)
a_floor = 2.3
# Assigned variable floor_output and use math to calculate floor calling variable a_floor
floor_output = math.floor(a_floor)
# Print the a_floor and floor_output value
print(f"For a = {a_floor}, floor of a is: {floor_output}")

# FACTORIAL
# Assigned variable a_factorial = 5 literal value 
a_factorial = 5
# Assigned variable factorial_output and use math to calculate floor calling variable a_factorial
factorial_output = math.factorial(a_factorial)
# Print a_factorial and factorial_output}
print(f"For a = {a_factorial}, factorial of a is: {factorial_output}")


# Assigned variable power_output and use math to calculate function () power with value of 2 and 3
power_output = math.pow(2, 3)
# Print the output - power of 2^3 calling the variable power_output}
print(f"For a = 2^3, the value is: {power_output}")

# Assigned variable a_squareroot value = 16
a_squareroot = 16
# Assigned variable a_squareroot and use math square root of value 16
squareroot_output = math.sqrt(a_squareroot)
# Print the value of 16 and print square root output 
print(f"For a = {a_squareroot}, square root of a is: {squareroot_output}")