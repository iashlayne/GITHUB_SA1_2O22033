# EXERCISE 1 - WELCOME GUI PROGRAM

import tkinter as tk
# Assigned variable "first_font_style" inside the tuples are "font style, font size, font weight"
first_font_style = ("Helvetica", 18, "bold")
second_font_style = ("Comic Sans MS", 20)

# Assigned a variable "current_font" = 1, initial font index
current_font = 1

# THIS IS THE FUNCTION where user clicks repeatedly change font it will switch to different font 
# style and size
# Defined a func() switch_font 
def switch_font():
    global current_font
    # If else condition
    # If the current_font is equals to 1
    if current_font == 1:
        # label.config is the text where it will switch between thw two fonts
        label.config(font=second_font_style, fg="#ffffff")
        current_font = 2
    # else it will switch index between 1 and 2
    else:
        label.config(font=first_font_style , fg="#ffffff")
        current_font = 1

# Assigned a variable "container" as tk.Tk() class to create window
container = tk.Tk()

# this is where the title of the window "Welcome to GUI Program"
container.title("Welcome to GUI Program")

# this is the size of the window "500x300"
container.geometry("500x300")

# this is to disable to resize the window boolean "False" and "False"
container.resizable(False,False)

# this is the background of the window .configure to modify the various property such as bg color
container.configure(background="#4D6661")

# this is the text for the gui widget "Welcome User to GUI PROGRAM, Have a Good Day!" 
# using the first font style setting the bg color and font color
label = tk.Label(container, text="Welcome User to GUI PROGRAM, Have a Good Day!" ,
                 font=first_font_style, bg="#4D6661", fg="#ffffff")
# this is to pack the label to the window using pady=30 to have a padding in y-axis direction
label.pack(pady=30)

# this is for the button "Change Font"
# Assigned variable "font_style_button" text as "Change Font" called the function
# (switch_font) when button clicked it will switch font, highlightbackground $ highlightcolor 
# to avoid the white border outside the button
font_style_button = tk.Button(container, text="Change Font", 
                              command=switch_font, borderwidth=0, highlightbackground="#4D6661",
                              highlightcolor="#4D6661")
# this is to the pack the button to the window using pady=15 to have a padding in y-axis direction 
font_style_button.pack(pady=15)

# To run the Tkinter event loop
container.mainloop()



    