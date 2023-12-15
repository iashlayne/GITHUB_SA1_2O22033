# Exercise 2 - Numpy Array

print("\n-----------------------------------------------")

# List the numbers
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
even_indices_numbers = [index for index, value in enumerate(a) if value % 2 == 0]
print("Indices of even numbers:", even_indices_numbers)

# Sort the array 
array_sort = sorted(a)
# Print the sort array 
print("Sorted array:", array_sort)

# Slice elements from index 3 to the end of the array
slice_end = a[3:]
# Print the Slice elements from index 3 to the end
print("Slice from index 3 to the end:", slice_end)

# Slice elements from index 0 to index 4
slice_index_from_0_4 = a[0:5]
# Print the Slice elements from index 0 to the index 4
print("Slice from index 0 to index 4:", slice_index_from_0_4)

# Print [32, 15, 67] using negative slicing
negative_slice_output = a[-5:-2]
# Print the negative slicing output
print("Using negative slicing:", negative_slice_output)

print("\n-----------------------------------------------")

