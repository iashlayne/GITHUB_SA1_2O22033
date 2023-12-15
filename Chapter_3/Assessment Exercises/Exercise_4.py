# EXERCISE 4 - AREA FUNCTION

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Assigned a class for the Shapes Area Calculator
class Calculate_Area_Shapes():
    def __init__(self, window):
        # Set the main window/frame
        self.window = window
        self.window.title("Shapes Area Calculator")
        
        # Used notebook to organize tabs
        self.notebook = ttk.Notebook(window)
        self.notebook.pack(fill="both", expand=True)
        
        # Make tabs for different shapes (circle, square and rectangle)
        self.make_circle_tab()
        self.make_square_tab()
        self.make_rectangle_tab()
    
    # Defined a method to calculate circle and create tab  
    def make_circle_tab(self):
        
        # Tab for circle
        circle_tab = ttk.Frame(self.notebook)
        self.notebook.add(circle_tab, text="Circle")
        
        # Input user - Circle radius even decimal
        self.circle_rad_var = tk.DoubleVar()
        
        # Label and entry for input radius from user using .pack() widget
        tk.Label(circle_tab, text="Input Radius:").pack(pady=10)
        enter_radius = tk.Entry(circle_tab, textvariable=self.circle_rad_var)
        enter_radius.pack(pady=5)
        
        # Area Calculate Button for shape circle
        button_circle_calculate = tk.Button (circle_tab, text="Calculate Area",
                                             command=self.circle_are_calculated)
        button_circle_calculate.pack(pady=10)
    
        
    # Defined a method to calculate square and create tab  
    def make_square_tab(self):
        
        # Tab for square
        square_tab = ttk.Frame(self.notebook)
        self.notebook.add(square_tab, text="Square")
        
        # Input user - Square side even decimal
        self.square_side_var = tk.DoubleVar()
        
        # Label and entry for input side from user using .pack() widget
        tk.Label(square_tab, text="Input Side:").pack(pady=10)
        enter_side = tk.Entry(square_tab, textvariable=self.circle_rad_var)
        enter_side.pack(pady=5)
        
        # Area Calculate Button for shape square
        button_square_calculate = tk.Button (square_tab, text="Calculate Area", 
                                             command=self.square_are_calculated)
        button_square_calculate.pack(pady=10)
        
    # Defined a method to calculate square and create tab  
    def make_rectangle_tab(self):
        
        # Tab for rectangle
        rectangle_tab = ttk.Frame(self.notebook)
        self.notebook.add(rectangle_tab, text="Rectangle")
        
        # Input user - rectangle length and width even decimal
        self.rectangle_len_var = tk.DoubleVar()
        self.rectangle_wid_var = tk.DoubleVar()
        
        # Label and entry for input length from user using .pack() widget
        tk.Label(rectangle_tab, text="Input Length:").pack(pady=5)
        enter_len = tk.Entry(rectangle_tab, textvariable=self.rectangle_len_var)
        enter_len.pack(pady=5)
        
        # Label and entry for input width from user using .pack() widget
        tk.Label(rectangle_tab, text="Input Width:").pack(pady=5)
        enter_len = tk.Entry(rectangle_tab, textvariable=self.rectangle_wid_var)
        enter_len.pack(pady=5)
        
        # Area Calculate Button for shape rectangle
        button_square_calculate = tk.Button (rectangle_tab, text="Calculate Area", 
                                             command=self.square_are_calculated)
        button_square_calculate.pack(pady=10)
        
    # Defined a method to calculate the data from user input - output are of circle
    def circle_are_calculated(self):
        try:
            radius = self.circle_rad_var.get()
            area = math.pi * radius **2
            messagebox.showinfo("Area Circle", f"The Area of Circle is {area:.2f}")
        except ValueError:
            messagebox.showerror("Error! Please enter a valid radius integer")
            
     # Defined a method to calculate the data from user input - output are of sqaure
    def square_are_calculated(self):
        try:
            side = self.square_side_var.get()
            area = side ** 2
            messagebox.showinfo("Area Square", f"The Area of Square is {area:.2f}")
        except ValueError:
            messagebox.showerror("Error! Please enter a valid side integer")
            
     # Defined a method to calculate the data from user input - output are of rectangle
    def rectangle_are_calculated(self):
        try:
            len = self.rectangle_len_var.get()
            wid = self.rectangle_wid_var.get()
            area = len * wid
            messagebox.showinfo("Area Rectangle", f"The Area of Rectangle is {area:.2f}")
        except ValueError:
            messagebox.showerror("Error! Please enter a valid length and width integer")

# Run tkinter event loop
if __name__ == "__main__" :
    window = tk.Tk()
    Calculate_Area_Shapes(window)
    window.mainloop()
    
   
    