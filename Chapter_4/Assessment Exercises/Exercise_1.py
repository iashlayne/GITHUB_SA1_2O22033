# CHAPTER 1 - USER INFORMATION

import tkinter as tk
from tkinter import messagebox

# Define function () save info for the user details 
def save_info():
    user_name = name_entry_entry.get()
    user_age = age_entry.get()
    user_hometown = hometown_entry.get()

    # To check the details have been completed if not it will show in message box "Error, 
    # complete details"
    if not user_name or not user_age or not user_hometown:
        messagebox.showerror("Error", "Please complete the details before proceeding.")
        return

    # This is when open messagebox to write the user's details, "w is for write" from bio.txt file
    with open("bio.txt", "w") as file:
        file.write(f"Name:{user_name}\nAge:{user_age}\nHometown:{user_hometown}")
        # This when details has been uploaded it will show your details have been save in bio.txt file
        messagebox.showinfo("File has been uploaded", "Your details have been saved to bio.txt")

# Defined a function read_data_file() 
def read_data_file():
    try:
        # This is when open messagebox to read the user's details, "r is for read" from bio.txt file
        with open("bio.txt", "r") as file:
            # Assigned variable "details" when file bio.txt using method() read to read the file
            details = file.read()
            # This is a pop-up message box when read from button clicks it will appear the details 
            # you hav$e saved
            messagebox.showinfo("File details", details)
    
    # Except when not save it will make error
    except FileNotFoundError:
        messagebox.showerror("File not found", "bio.txt not found. "
                                "Please save your details first.")

# Assigned a variable window for the frame using class Tk()
window = tk.Tk()

# Title of the frame
window.title("Users Bio Information")

window.geometry("350x350")

# Background color of the frame
window.configure(bg="#416366")

# Name: 
# Name label contains in the window text "Name" bg color, font style and size, text color fg=""
name_label = tk.Label(window, text="Name:", bg="#416366", font=("Helvetica", 15), fg="white")

# Name: - position in grid manner
name_label.grid(row=0, column=0, padx=10, pady=15)

# ▬ Name Input  - in the window and bg color
name_entry_entry = tk.Entry(window, bg="#96DEE5")

# ▬ Name input = position in grid manner
name_entry_entry.grid(row=0, column=1, padx=10, pady=15)

# Age:
# Age label contains in the window text "Age" bg color, font style and size, text color fg=""
age_label = tk.Label(window, text="Age", bg="#416366", font=("Helvetica", 15), fg="white")

# Age: - position in grid manner
age_label.grid(row=1, column=0, padx=10, pady=15)

# ▬ Age input  - in the window and bg color
age_entry = tk.Entry(window, bg="#96DEE5")

# ▬ Age input = position in grid manner
age_entry.grid(row=1, column=1, padx=10, pady=15)

# Hometown:
# Hometown label contains in the window text "Hometown" bg color, font style and size, text color fg=""
hometown_label = tk.Label(window, text="Hometown:", bg="#416366", font=("Helvetica", 15), fg="white")

# Hometown: - position in grid manner
hometown_label.grid(row=2, column=0, padx=10, pady=15)

# ▬ Hometown input  - in the window and bg color
hometown_entry = tk.Entry(window, bg="#96DEE5")

# ▬ Hometown input = position in grid manner
hometown_entry.grid(row=2, column=1, padx=10, pady=15)

# Save details - button 
# Save button, calling the function save_info to save details of the user, highlightbackground= color
save_file_button = tk.Button(window, text="Save details", command=save_info,
                             highlightbackground="#416366")

# Save details button - position in grid manner
save_file_button.grid(row=3, column=0, columnspan=2, pady=15)

# Read details - button 
# Read button, calling the function read_data_file to save details of the user,
# highlightbackground= color
read_file_button = tk.Button(window, text="Read details", command=read_data_file, 
                             highlightbackground="#416366")

# Read details button - position in grid manner
read_file_button.grid(row=4, column=0, columnspan=2, pady=15)

# To run the Tkinter event loop
window.mainloop()