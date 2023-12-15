# EXERCISE 5 - CALCULATOR

import tkinter as tk
# This is for messagebox is a pop-up and text said upon various functions
from tkinter import messagebox

# Defined a function math_operators()
def math_operators():
    try:
        # Assigned a variable number_1 = (user input 1st number) float ()class (enter_num1) 
        # which will be used for widget user entry
        # get() method to return data from entry widget to print later on
        number_1=float(enter_num1.get())
        
        # Assigned a variable number_2 = (user input 2nd number) float ()class (enter_num1)
        # which will be used for widget user entry
        # get() method to return data from entry widget to print later on
        number_2=float(enter_num2.get())
        
        # If elif else condition
        
        # Addition If operator.get() "+" method to return data from entry widget to print later on
        if operator.get() == "+":
            # Assigned variable "output" from user input number_1 + number_2 performs addition
            output = number_1 + number_2
            # Assigned variable "output_message" when two numbers has been added calling the "output" 
            # variable and calculated this message will pop up in the messagebox
            output_message = f"The sum is {output}"
        
        # Subtraction Elif operator.get() "-" method to return data from entry widget to print later on
        elif operator.get() == "-":
            # Assigned variable "output" from user input number_1 - number_2 performs subtraction
            output = number_1 - number_2
            # Assigned variable "output_message" when two numbers has been subtracted calling the
            # "output" variable and calculated this message will pop up in the messagebox
            output_message = f"The difference is {output}"
            
        # Multiplication Elif operator.get() "*" method to return data from entry widget 
        # to print later on
        elif operator.get() == "*":
            # Assigned variable "output" from user input number_1 x number_2 performs multiplication
            output = number_1 * number_2
            # Assigned variable "output_message" when two numbers has been multiplied calling 
            # the "output" variable and calculated this message will pop up in the messagebox
            output_message = f"The product is {output}"
            
        # Division Elif operator.get() "/" method to return data from entry widget to print later on
        elif operator.get() == "/":
            # If number_2 is equals to 0
            if number_2 == 0:
                # It will raise it cannot divide by zero
                raise ZeroDivisionError("Cannot divide by zero.")
            # Assigned variable "output" from user input number_1 / number_2 performs division
            output = number_1 / number_2
            # Assigned variable "output_message" when two numbers has been divided calling the
            # "output" variable and calculated this message will pop up in the messagebox
            output_message = f"The quotient is {output}"
            
        # Modulo Elif operator.get() "/" method to return data from entry widget to print later on
        elif operator.get() == "%":
            # Assigned variable "output" from user input number_1 % number_2 performs modulo
            # "getting remainder"
            output = number_1 % number_2
            # Assigned variable "output_message" when two numbers has been modulo calling
            # the "output" variable and calculated this message will pop up in the messagebox
            output_message = f"The modulo is {output}"
        # else it will raise value error, in message box "Try again, Invalid Operation"
        else:
            raise ValueError("Try again, Invalid Operation")
        
        # This is to show the result depending on the operation you choose to calculate from
        # "output_message"
        messagebox.showinfo("Result", output_message)
    # When user type any other keys than integers it will make error" "Try Again, 
    # Please enter a valid integer"
    except ValueError:
        messagebox.showerror("Error:", "Try Again, Please enter a valid integer.")
    # This is when zero is also has been typed it will tell that it cannot divided by zero
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")

# Creating the main frame/window   
window = tk.Tk()

# this is where the title of the window "Calculator"
window.title("Calculator")

# background color of the frame 
window.configure(bg="#F08A2D")

# # this is to disable to resize the window boolean "False" and "False"
window.resizable(False, False)


# this is the text for the gui widget "Calculator" setting the bg color and 
# font color, font style, font size, text color fg="", pady= y axis 
label_title = tk.Label(window, text="Calculator", font=("Helvetica", 18, "bold"), bg="#F08A2D",
                       fg="white", pady=10)

# this for the positioning of the word "Calculator" in row, column, columnspan and sticky 
label_title.grid(row=0, column=0, columnspan=2, sticky="n")

# Enter your 1st number:
# this is the text for the gui widget "Enter your 1st number" setting the bg color 
# and font color,text color fg=""
label_num1 = tk.Label(window, text="Enter your 1st number:", bg="#F08A2D", fg="white")
# this is for the entry - user input bg color of the 1st number to avoid white highlights
enter_num1 = tk.Entry(window, bg="#EFA357")

# Enter your 2nd number:
# this is the text for the gui widget "Enter your 2nd number" setting the bg color and 
# font color,text color fg=""
label_num2 = tk.Label(window, text="Enter your 2nd number:", bg="#F08A2D", fg="white")
# this is for the entry - user input bg color of the 1st number to avoid white highlights
enter_num2 = tk.Entry(window, bg="#EFA357")

# Select your operator
# This is for user to choose select your operator setting bg color and text color fg=""
label_operator = tk.Label(window, text="Select your operator", bg="#F08A2D", fg="white")

# This is where the operator is set to tk.StringVar() to convert the text to include numbers,
# letters or even symbols
operator = tk.StringVar()

# This to set the main when window is open using the method set() operator used
operator.set("+")
# Using OptionMenu class contains inside the window and choices in the operator from the function
# "+", "-", "*", "/", "%"
operator_choice = tk.OptionMenu(window, operator, "+", "-", "*", "/", "%")
# This to set  bg color and avoid white highlights
operator_choice.config(bg="#F08A2D")

# Calculate
# This to set the calculate button inside the window is the color text calling command= math 
# operators function() to process the calculation
button_calculate = tk.Button(window,highlightbackground="#F08A2D", text="Calculate", 
                             command=math_operators)

# Enter your 1st number:
# Position the word Enter your 1st number: in grid manner
label_num1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# ▬ User input - 1st number
# Position the input 1st number box in grid manner
enter_num1.grid(row=1, column=1, padx=10, pady=10)

# Enter your 2nd number:
# Position the word Enter your 2nd number: in grid manner
label_num2.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# ▬ User input - 2nd number
# Position the input 2nd number box in grid manner
enter_num2.grid(row=2, column=1, padx=10, pady=10)

# Select your operator 
# Position the word "Select your operator" box in grid manner
label_operator.grid(row=3, column=0, padx=10, pady=10, sticky="e")

# "+", "-", "*", "/", "%" 
# Position the operation menu in grid manner
operator_choice.grid(row=3, column=1, padx=10, pady=10)

# Calculate
# # Position the calculate button in grid manner
button_calculate.grid(row=4, column=1, pady=10)

# To run the Tkinter event loop
window.mainloop()





        
         
         
        

        