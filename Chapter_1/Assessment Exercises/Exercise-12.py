#EXERCISE 12 - AREA FUNCTION

#We define a variable user_select and an input function for a user to choose a shape to calculate, 
# .lower() to make it case-insensitive
print("\n***********************************************")
user_select=str(input("Choose a Shape you that you want to calculate : "
"\n \n a. Circle \n b. Rectangle \n c. Triangle \n \n " )).lower()

#If user select a - Circle shape is chosen
   #If user choose a - Area of Circle will calculate
if user_select== "a":
      print("\nYou choose CIRCLE ○ ")
      radius=float(input(" \n Input the radius: "))
      c_area=3.14*radius**2
      print("\n The Area of Circle: ", c_area)
      print("***********************************************")

#elif user select a - Rectangle shape is chosen      
   #If user choose a - Area of Rectangle will calculate
elif user_select== "b":
      print("\nYou choose RECTANGLE ▭ ")
      length=float(input("\n Input the length: "))
      width=float(input(" Input the width:  "))
      r_area=length * width
      print("\n The Area of Rectangle: ", r_area)
      print("***********************************************")
  
      
#If user select a - Triangle shape is chosen      
    #If user choose a - Area of Triangle will calculate
elif user_select== "c":
         print("\nYou choose Triangle △ ")
         base=float(input("\n Input the base: "))
         height=float(input(" Input the height: "))
         t_area=(1/2)*base*height
         print("\n The Area of Triangle: ", t_area)
         print("***********************************************")

#else, If the user input wrong data it will print "Your Input is invalid, choose only a, b and c"
else:
   print("------Your input is invalid, choose only a, b and c------")
         