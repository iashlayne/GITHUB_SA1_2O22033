# EXERCISE 5 - PASSWORD CHECK

import tkinter as tk
from tkinter import messagebox
import re

# Created a class Password_Check() which will be called later on 
class Password_Check():
    # Define a method using self variable to be called later on and window to be use for the 
    # window properties
    def __init__(self, window):
        self.window = window
        # Title of the Frame "Password Check GUI App"
        self.window.title("Password Check GUI App")
        self.window.configure(bg="black")
        # Size of the window/frame "500x300"
        self.window.geometry("500x300")
        
        # Enter password using class Label() inside window contains text, font style and 
        # size bg color and text color
        enter_password = tk.Label(window, text="Enter your password:", 
                                  font=("Comic Sans", 18, "bold"), bg="black", fg="yellow")
        
        # Enter password postion in pack() widget
        enter_password.pack(pady=10)
        
        # When password type it will be seen as "*"
        self.password_entry = tk.Entry(window, show="*")
        # ▬  password_entry postion in pack() widget
        self.password_entry.pack(pady=5)
        
        # This note for user to know what to input to make the password valid like a warning text,
        # bg color and text color
        password_note = tk.Label(window, text ="Min: 6, Max: 12, Must have at least one uppercase," 
                                 "character and number.", bg="black", fg="red")
        
        # password_note position in pack() widget
        password_note.pack(pady=20)
        
        # Verify Password Button 𓋰 - when click it will call command the check_password 
        # if it is valid and the requirements needed is entered
        verify_password = tk.Button(window, text="Verify Password", 
                                    command=self.check_password, highlightbackground="black")
        # Verify Password Button 𓋰  in pack() widget
        verify_password.pack(pady=30)
    
    # Define a method () check_password to check if the details entered are correct 
    def check_password(self):
        password = self.password_entry.get()
        # If not 6 is greater, equals than between less, eqauls 12 than the length password
        # will show invalid and try again
        if not (6 <= len(password) <= 12):
            messagebox.showwarning("Invalid Password", 
                                   "Password must contain at least between 6 and 12 characters.")
            return
        # If not a-z is not entered will show invalid and try again
        if not re.search("[a-z]", password):
            messagebox.showwarning("Invalid Password", 
                                   "Password must have at least 1 lowercase letter")
            return
        
        # If not A-Z is not entered will show invalid and try again
        if not re.search("[A-Z]", password):
            messagebox.showwarning("Invalid Password", 
                                   "Password must have at least 1 uppercase letter")
            return
        
        # If not 0-9 is not entered will show invalid and try again
        if not re.search("[0-9]", password):
            messagebox.showwarning("Invalid Password", 
                                   "Password must have at least 1 valid number")
            return
        
        # If not $,#,%,!,& these special char is not entered will show invalid and try again
        if not re.search("[$#%!&]", password):
            messagebox.showwarning("Invalid Password", 
                                   "Password must have at least 1 of this special" 
                                   "character $, #, %, !, &")
            return
        
        # If you completed the details correctly, Messagebox will show password is valid.
        messagebox.showinfo("Password Valid", 
                            "Your password is valid!")

# # To run the Tkinter event loop
if __name__ == "__main__":
    window = tk.Tk()
    Password_Check(window)
    window.mainloop()


        
        
        