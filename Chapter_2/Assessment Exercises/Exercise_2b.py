# EXERCISE 2 - MANAGING LAYOUT
# 2b - using grid()

from tkinter import *
import tkinter as tk

# Assigned a variable window for the frame using class Tk()
window = tk.Tk()

# Title of the frame "Managing Layout - Square Grdd"
window.title("Managing Layout - Square Grid")

# FRAME - LEFT SIDE

# Assigned a variable left_frame in window(tk) bd(border=5) bg=(#A0A0A0 relief(style of button=solid)
left_frame = tk.Frame(window, relief="solid", bg="gray", highlightthickness=4, padx=5, pady=5)


# called variable "left_frame" using .pack to organize frame (side=left), (fill = both to fill x 
# and y axis), expand = yes
left_frame.pack(side="left", fill="both", expand="TRUE")

# FRAME - RIGHTSIDE

# Assigned a variable right_frame in window(tk) bd(border=5) bg=(#A0A0A0 relief(style of button=solid)
right_frame = tk.Frame(window, relief="solid", bg="gray", highlightthickness=4, padx=5, pady=5)

# called variable "right_frame" using .pack to organize frame (side=right), (fill = both to fill x 
# and y axis), expand = yes 
right_frame.pack(side="right", fill="both", expand="TRUE")

# A-B-C-D squares


# Assigned variable a_button using tk. class() Label called the variable "left-frame" contains text=A,
# bg(background color = #242b40) fg(foreground/text color= white) padx(padding horizontally) 
# and pady(padding vertitally)
a_button = tk.Label(left_frame, text="A", bg="#242B40", fg="white", padx=10, pady=10)

# Called the variable a_button using .pack() to organize square (side = top), (fill = both to fill x 
# and y axis), expand = yes
a_button.pack(side="top", fill="both", expand="YES")

# Assigned variable b_button using tk. class() Label called the variable "left-frame" contains text=B,
# bg(background color = white) fg(foreground/text color= black) padx(padding horizontally) 
# and pady(padding vertitally)
b_button = tk.Label(left_frame, text="B", bg="white", fg="black", padx=10, pady=10)

# Called the variable b_button using .pack() to organize square (side = bottom),
# (fill = both to fill x and y axis), expand = yes
b_button.pack(side="bottom", fill="both", expand="YES")

# Assigned variable c_button using tk. class() Label called the variable right-frame" contains text=C,
# bg(background color = #242b40) fg(foreground/text color= white) padx(padding horizontally) 
# and pady(padding vertitally)
c_button = tk.Label(right_frame, text="C", bg="white", fg="black", padx=10, pady=10)

# Called the variable c_button using .pack() to organize square (side = top), (fill = both to 
# fill x and y axis), expand = yes
c_button.pack(side="top", fill="both", expand="YES")

# Assigned variable d_button using tk. class() Label called the variable "right-frame" contains text=D,
# bg(background color = white) fg(foreground/text color= black) padx(padding horizontally) and 
# pady(padding vertitally)
d_button = tk.Label(right_frame, text="D", bg="#242B40", fg="white", padx=10, pady=10)


# Called the variable d_button using .pack() to organize square (side = bottom), 
# (fill = both to fill x and y axis), expand = yes
d_button.pack(side="bottom", fill="both", expand="YES")

# run the tkinter event loop
window.mainloop()