# EXERCISE 2 - MANAGING LAYOUT
# 2a - using pack()

import tkinter as tk
# Assigned a variable window for the frame using class Tk()
window = tk.Tk()

# Title of the frame "Managing Layout - Using Pack"
window.title("Managing Layout - Using Pack")

# I used label because apparently the button is not making any changes

# Assigned a variable "a_button" as label (button) in the frame which (window) contains text=A,
# bg(background=red), relief(style of button=sunken), bd(border=5)
a_button = tk.Label(window, text="A", bg="red", relief="sunken", bd=5)

# calling a_button and using .pack() to organize the buttons, side=top, expand=yes,
# fill = x (fill horizontally)
a_button.pack(side="top", expand = "YES", fill="x")

# Assigned a variable "b_button" as label (button) in the frame which (window) contains text=B,
# bg(background=yellow), relief(style of button=flat), bd(border=3), width=10
b_button = tk.Label(window, text="B", bg="yellow", relief="flat", bd=3, width=10)

# calling a_button and using .pack() to organize the buttons, side=bottom, expand=no
b_button.pack(side="bottom", expand="NO")

# Assigned a variable "c_button" as label (button) in the frame which (window) contains text=C,
# bg(background=blue), relief(style of button=flat), bd(border=2), width = 10
c_button = tk.Label(window, text="C", bg="blue", relief="flat", bd=2, width=10)

# calling a_button and using .pack() to organize the buttons, side=left, expand=yes, fill=none, 
# anchor=se(south east)
# padx (means padding in x axis = 0)
c_button.pack(side="left", expand="YES", fill='none', anchor='se', padx=0)

# Assigned a variable "a_button" as label (button) in the frame which (window) contains text,
# bg(background), relief(style of button), bd(border)
d_button = tk.Label(window, text="D", bg="white", relief="flat", bd=2, width=10)
# calling a_button and using .pack() to organize the buttons, side=right, expand=yes, fill=none,
# anchor=se(south east)
# padx (means padding in x axis = 0)
d_button.pack(side="right", expand="YES", fill='none', anchor='se', padx=0)

# run the tkinter event loop
window.mainloop()