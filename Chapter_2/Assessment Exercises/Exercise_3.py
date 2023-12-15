# EXERCISE 3 - MANAGING LAYOUT
# using grid()
import tkinter as tk
from tkinter import messagebox


# Define a function login_section()
def login_section():
    # Assigned a variable "user_name" 
    user_name = enter_username.get()
    pass_word = enter_password.get()
    
    
    login_message = (f"Login Successfully\nUsername:{user_name}\nPassword:{pass_word}")
    messagebox.showinfo("Success",login_message)

# Creating the main frame/window    
window = tk.Tk()

# Title of the frame
window.title("LogIn Page")

# Setting the initial size of the frame
window.geometry("350x200")

# Setting the background color of the frame
window.configure(bg="#555555")

# this is to disable to resize the window boolean "False" and "False"
window.resizable(False, False)

# Assigned a variable "label_greet" calling tk. class() label contains inside the window
# WELCOME USER - LOG IN PAGE with its text properties and paddy= padding in y axis
label_greet = tk.Label(window, text="LOG-IN",bg="#555555", 
                       font=("Helvetica", 18,"bold"), pady=10, fg="white")
# Assigned a variable "label_user_name" calling tk. class() label contains inside the window
# text= username, bg = bg color, and fg = text color
label_user_name = tk.Label(window, text="Username:", bg="#555555", fg="white")
# Assigned a variable "label_user_password" calling tk. class() label contains inside the window
# text= username, bg = bg color, and fg = text color
label_pass_word = tk.Label(window, text="Password:", bg="#555555", fg="white")

# ENTRY - for user input
# Assigned a variable "label_user_name" calling tk. class() entry widget contains inside the window
# bg color of the box
enter_username = tk.Entry(window, bg="#59A1B3")
# Assigned a variable "label_user_password" calling tk. class() entry widget contains inside the window
# bg color of the box and show="*" when user type password it will be hidden as *
enter_password = tk.Entry(window, show="*", bg="#59A1B3")

# Assigned a variable login_button calling tk. class() button widget contains inside the window
# text= Login when clicked command="login_section" <-- calling the function, highlightbackground= color
login_button = tk.Button(window, text="Login", command=login_section, highlightbackground="#555555")

# Using grid geometry such as columns and rows

# CALCULATOR
# called variable label_greet.grid method(row, columnspan = to occupy numbers of column in grid, 
# sticky= to tell where the cell where sticks "n"-north)
label_greet.grid(row=0, column=0, columnspan=2, sticky="n")

# Username:
# called variable label_greet.grid method(row, column padx and pady = spacing in x and y axis,
# sticky= to tell where the cell where sticks "e"-east)
label_user_name.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# ▬ User input - username 
# called variable enter_username.grid method(row, column padx and pady = spacing in x and y axis,
# sticky= to tell where the cell where sticks "ew"-east west)
enter_username.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Password:
# called variable label_pass_word.grid method(row, column padx and pady = spacing in x and y axis, 
# sticky= to tell where the cell where sticks "e"-east)
label_pass_word.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# ▬ User input - password
# called variable enter_password.grid(row, column padx and pady = spacing in x and y axis, sticky=
# to tell where the cell where sticks "ew"-east west)
enter_password.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# 𓋰 - LogIn Button login_button.grid(row, column, columnspan = to occupy numbers of column in grid,
# pady= spacing in y axis)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# To run the Tkinter event loop
window.mainloop()



