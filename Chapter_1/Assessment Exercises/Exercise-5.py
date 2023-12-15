# EXERCISE 5 - CONTINUE

#Print the intro - CONTINUE GAME
print("\n*-*-*-*-*-*-*-*-*-*-*-* CONTINUE GAME *-*-*-*-*-*-*-*-*-*-*-*\n")

# Defined a function main
def main():
    # assigned a variable "count" and its value 0
    count = 0
    
    # While loop - While the loop is true:
    while True:
        # assigned a variable "user_Y" and funct(input) where it will ask the user 
        # to press y to continue 
        # if user want to exit print different key
        user_Y = input("Would you like to continue? Press 'Y' to continue, press different key to exit : ")
        # the variable "count" += 1 is increased by 1 each iteration 
        count += 1
        
        # if condition, the user input converted the "y" to "Y" uppercase to avoid case sensitive
        # if user entered any other keys than "Y" and the break will be executed
        if user_Y.upper() != 'Y':
            break
    
    #Print how many Y's has been counted while the loop is on run.
    print("\n--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞")        
    print(f"The while loop lasted {count} times.")
    print("--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞--∞\n")     

# if __name__ is a variable in python where script is executed
# __name__ set to __main__ if function (main) the program being run
if __name__ == "__main__":
    main()
    
    
    
    
    