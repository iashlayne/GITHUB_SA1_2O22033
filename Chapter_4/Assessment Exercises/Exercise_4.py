# EXERCISE 4 - LETTER COUNT
# GUI

import tkinter as tk
# This is function from library for file input from your folder
from tkinter import filedialog

# This check for the open file 
def check_file():
    global file_path
    # function from library
    file_path = filedialog.askopenfilename()
    
# defined function read content file, retrieves chracter from user input, to count the stored character,
# iterate lines in content, counts the occurence of string and update the system
def character_count():
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            character = character_entry.get()
            count = 0
            for line in lines:
                count += line.count(character)
            output_label.config(text=f"The character '{character}' occurs {count} times.")
    except FileNotFoundError:
        output_label.config(text="Error: The specified file could not be found.")

# Create tkinter root frame
root = tk.Tk()

# Title of frame/root
root.title("Character Counter")

# Bg color of frame
root.configure(bg="lightsalmon")

# Assigned variable instructions_label contains inside the window text properties, bg color
instructions_label = tk.Label(root, text="Please follow these steps:", font=("Arial", 18, "bold"),
                              bg="lightsalmon")

# Use pack () widget and padding in y axis
instructions_label.pack(pady=10)

# Assigned variable label_file contains inside the window text properties, bg color
label_file = tk.Label(root, text="1. Open the file 'sentences.txt' using the 'Open' button.",
                      font=("Arial", 15), bg="lightsalmon")
# Use pack () widget and padding in y axis
label_file.pack(pady=10)

# Assigned variable open_button contains inside the window text, highlightbg
open_button = tk.Button(root, text="Open", command=check_file, highlightbackground="lightsalmon")
# Use pack () widget and padding in y axis
open_button.pack(pady=10)

# Assigned variable label_character_count contains inside the window text properties, bg color
label_character_count = tk.Label(root, text="2. Input the character you want to count in the "
                                 "'Character' entry box.", font=("Arial", 15), bg="lightsalmon")
# Use pack () widget and padding in y axis
label_character_count.pack(pady=10)

# Data entry for character from user bg color
character_entry = tk.Entry(root, bg="lightblue")
# Use pack () widget and padding in y axis
character_entry.pack(pady=10)

# Assigned variable count_button for Button Count calling command character_count when triggered.
# highlight bg
count_button = tk.Button(root, text="Count", command=character_count, highlightbackground="lightsalmon")
# Use pack () widget and padding in y axis
count_button.pack(pady=15)

# This is to display the final count of the string occurence from user input
output_label = tk.Label(root, text="")
# Use pack () widget and padding in y axis
output_label.pack()

# Run the main loop
root.mainloop()