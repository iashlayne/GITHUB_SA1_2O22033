# Exercise 2 - Student Class

import tkinter as tk
from tkinter import messagebox

# Created a class "Students" which will be called later on
class Students:
    def __init__(self, student_name, mark_1, mark_2, mark_3):
        self.student_name = student_name
        self.mark_1 = mark_1
        self.mark_2 = mark_2
        self.mark_3 = mark_3
        
    # Define a method to add the grades and calculate by 3
    def calculate_grade(self):
        students_average = (self.mark_1 + self.mark_2 + self.mark_3) / 3
        # Return student average
        return students_average
    
    # Define a method to display the student name and average grade from user input
    def display(self):
        return f"Student's Name: {self.student_name}\nAverage Grade: {self.calculate_grade()}"

def input_students_details():
    # Create a main window
    input_window = tk.Tk()
    # Title
    input_window.title("Student's Data Input")
    input_window.configure(bg="#303C4C")

    # Entry variables for using class StringVar()
    student_name_var = tk.StringVar()
    mark_1_var = tk.DoubleVar()
    mark_2_var = tk.DoubleVar()
    mark_3_var = tk.DoubleVar()

    # Widgets GUI
    # Students name :
    # properties text, bg color , text color
    tk.Label(input_window, text="Student Name:", font=("Comic Sans Ms", 16, "bold"), bg="#303C4C", 
             fg="white").pack(pady=10)
    # Students name = user-input
    student_name_entry = tk.Entry(input_window, textvariable=student_name_var, bg="#DFCDEE")
    # Students name user input position using pack() widget
    student_name_entry.pack(pady=10)

    # Enter your 1st Mark:
    # properties text, bg color , text color
    tk.Label(input_window, text="Enter your 1st Mark:", font=("Comic Sans Ms", 14), bg="#303C4C",
             fg="#E6A3B2").pack(pady=10)
    # Enter your 1st Mark: - user input
    mark_1_entry = tk.Entry(input_window, textvariable=mark_1_var, bg="lightyellow",
                            highlightbackground="#303C4C")
    # Enter your 1st Mark: - user input position using pack() widget
    mark_1_entry.pack(pady=10)

    # Enter your 2nd Mark:
    # properties text, bg color , text color
    tk.Label(input_window, text="Enter your 2nd Mark:", font=("Comic Sans Ms", 14),
             bg="#303C4C", fg="#E6A3B2").pack(pady=10)
    # Enter your 2nd Mark: - user input
    mark_2_entry = tk.Entry(input_window, textvariable=mark_2_var, bg="lightyellow" , 
                            highlightbackground="#303C4C")
    # Enter your 2nd Mark: - user input position using pack() widget
    mark_2_entry.pack(pady=10)
    
    # Enter your 3rd Mark:
    # properties text, bg color , text color
    tk.Label(input_window, text="Enter your 3rd Mark:", font=("Comic Sans Ms", 14),
             bg="#303C4C", fg="#E6A3B2").pack(pady=10)
    # Enter your 3rd Mark: - user input
    mark_3_entry = tk.Entry(input_window, textvariable=mark_3_var, bg="lightyellow", 
                            highlightbackground="#303C4C")
    # Enter your 3rd Mark: - user input position using pack() widget
    mark_3_entry.pack(pady=10)

    # Call function display_students_details when the "Show Data" button is clicked
    def display_students_details():
        student_name = student_name_var.get()
        mark_1 = mark_1_var.get()
        mark_2 = mark_2_var.get()
        mark_3 = mark_3_var.get()

        # Create the student object
        student = Students(student_name, mark_1, mark_2, mark_3)

        # Display student info
        details = student.display()
        messagebox.showinfo("Student's Data", details)

        # Closing the input window to show data
        input_window.destroy()

    # Button to trigger click display_students_details function
    show_button = tk.Button(input_window, text="Show Data", command=display_students_details, 
                            highlightbackground="#303C4C")
    show_button.pack(pady=40)

    # Run the input window event loop
    input_window.mainloop()

# Call the input_students_details function
input_students_details()