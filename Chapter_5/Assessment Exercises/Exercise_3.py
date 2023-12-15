# Exercise 3 - Employee Class

import tkinter as tk
from tkinter import messagebox

# Employee_Details class to store information about each employee
class Employee_Details():
    def __init__(self, name, position, salary, employee_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = employee_id
    
    # Method to get formatted information about the employee
    def getInfo(self):
        return f"{self.name}\t\t{self.position}\t\t{self.salary}\t\t{self.employee_id}"

# Employee_Widget class for creating the GUI and managing employee data
class Employee_Widget():
    def __init__(self, window):
        self.window = window
        self.window.title("Employees Data Entry")
        self.window.geometry("400x600")
        
        self.employees_list = []  # List to store employee objects
        
        self.make_widgets()  # Initialize and create GUI widgets

    # Method to create GUI widgets
    def make_widgets(self):
        tk.Label(self.window, text="Employee's Data Entry", font=("Helvetica", 18, "bold")).pack(pady=10)
        
        self.label_employee = tk.Label(self.window, text="", font=("Helvetica", 12))
        self.label_employee.pack(pady=10)
        
        self.name_var = tk.StringVar()
        self.position_var = tk.StringVar()
        self.salary_var = tk.DoubleVar()
        
        tk.Label(self.window, text="Name:").pack(pady=5)
        tk.Entry(self.window, textvariable=self.name_var).pack(pady=5)
        
        tk.Label(self.window, text="Position:").pack(pady=5)
        tk.Entry(self.window, textvariable=self.position_var).pack(pady=5)
        
        tk.Label(self.window, text="Salary:").pack(pady=5)
        tk.Entry(self.window, textvariable=self.salary_var).pack(pady=5)
        
        tk.Button(self.window, text="Add Employee", command=self.add_employee).pack(pady=10)
        tk.Button(self.window, text="Show Employees", command=self.display_employee_list).pack(pady=10)
        
    # Method to add a new employee to the list
    def add_employee(self):
        name = self.name_var.get()
        position = self.position_var.get()
        salary = self.salary_var.get()
        employee_id = len(self.employees_list) + 1
    
        employees = Employee_Details(name, position, salary, employee_id)
        self.employees_list.append(employees)
        
        messagebox.showinfo("Employee Added", f"{name} is added successfully")
        
        self.name_var.set()  # Clear the entry for the next input
        self.position_var.set()  # Clear the entry for the next input
        self.salary_var.set(0.0)  # Clear the entry for the next input
    
    # Method to display the list of employees
    def display_employee_list(self):
        if not self.employees_list:
             messagebox.showwarning("No added employees", "No Data Entry Employee to be shown.")
             return
         
        result = "Name\t\tPosition\t\tSalary\t\tID\n"
        for employees in self.employees_list:
             result += employees.getInfo() + "\n"
             
        self.label_employee.config(text=result)

# Entry point for the program
if __name__ == "__main__":
    window = tk.Tk()
    Employee_Widget(window)  # Initialize the GUI
    window.mainloop()
