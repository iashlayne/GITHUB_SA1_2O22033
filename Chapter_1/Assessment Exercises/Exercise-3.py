# EXERCISE 3 - IS IT TRIANGLE

# Defined a function "types_triangle" to if elif condition from side a , side b , and side c
# from the user input
def types_triangle(sidea, sideb, sidec):
    # If side a = side b = side c (3 sides equal) - classified as "EQUILATERAL" triangle
    if sidea == sideb == sidec:
        return "Equilateral Triangle ▲"
    # If side a = side b , side a = side c, side b = side c (2 sides equal, 1 is not) - 
    # classified as "ISOSCELES" triangle
    elif sidea == sideb or sidea == sidec or sideb == sidec:
        return "Isosceles Triangle ◤ "
    # If side a ≠ side b ≠ side c (3 different sides) - classified as "SCALENE" triangle
    elif sidea != sideb != sidec:
        return "Scalene Triangle ◣ "

# Defined a function main
def main():
    # Print to classify which triangle is it
    print("------------------------------------------------------------")
    print("CLASSIFY TRIANGLE - Isosceles ◤ , Scalene ◣ , Equilateral ▲\n")
    # Print the length of 3 sides of triangle
    print("Enter the length of three sides of the Triangle ")
    
    #Input the side a, side b, and side c - using float where user can input decimal numbers/integers 
    sidea = float(input("\nEnter the length of side a:"))
    sideb = float(input("Enter the length of side b:"))
    sidec = float(input("Enter the length of side c:"))
    
    # Assigned a variable "variety_triangle" called the func (types_triangle) if its classified as
    # Isosceles or  Scalene or Equilateral based from the user input side a, side b, and side c
    variety_traingle = types_triangle(sidea, sideb, sidec)
    
    # print which type of triangle from variable "variety_triangle"
    print(f"\nClassify : {variety_traingle}")
    
    # print for design purpose
    print("----------------THANK YOU, HAVE A NICE DAY!------------------") 
    
# if __name__ is a variable in python where script is executed
# __name__ set to __main__ if function (main) the program being run
if __name__ == "__main__":
    main()
    


    
    
    