# BONUS EXERCISE
#EXERCISE B - LOCATIONS LIST
print("\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* BONUS *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Print orginal list, find the length of list locatio s
print("\nOriginal List:", locations)
print("\nLength of the List:", len(locations))

# Used func() sorted to sort locations without modyfing the orig list
sorted_alphabetical = sorted(locations)
# Print sort alphabetically:
print("\nSorted Alphabetically:", sorted_alphabetical)

# Print the actual list which is unchanged showing the actual order of locations
print("\nOriginal List (unchanged):", locations)

# Use sorted locations but in reverse = True which prints in actual list but in reverse manner
sorted_reverse = sorted(locations, reverse=True)
print("\nSorted in Reverse Alphabetical Order:", sorted_reverse)

# Print the actual list to show it is still in original order
print("\nOriginal List (unchanged):", locations)

# Use reverse() method to change the actual list order
locations.reverse()
print("\nReversed List:", locations)

# Use sort() changing the list in alphabetical manner
locations.sort()
print("\nList Sorted Alphabetically:", locations)

# Use sort() changing the list in reverse alphabetical manner
locations.sort(reverse=True)
print("\nList Sorted in Reverse Alphabetical Order:", locations)

print("\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")