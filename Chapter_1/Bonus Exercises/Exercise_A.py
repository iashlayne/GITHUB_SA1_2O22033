# BONUS EXERCISE
#EXERCISE A - MULTIPLICATION TABLE

print("\n\n----------------- BONUS -----------------------\n")
# Outer loop - For x variable loop in range of 1-10
for x in range(1,11):
    
    print("Multiplication table of:")
    # Inner loop - For y variable loop in range of 1-10
    for y in range(1, 11):
        # Output x times y
        output = x * y
        # Print the output from range1 to 10 multiplication
        print(f"{x} x {y} = {output}")
        
    # print the nested loop
    print()
    
print("\n\n------------------------------------------------\n")