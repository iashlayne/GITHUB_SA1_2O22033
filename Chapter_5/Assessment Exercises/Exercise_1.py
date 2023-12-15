# Exercise 1 - Woof Woof
import tkinter as tk
from tkinter import messagebox

# Class Dog Info self(variable) dog_name , dog_age
class Dog_Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Function to woof woof!
    def woof(self):
        return "Woof! Woof! Woof!"
# Class Dog_Widget
class Dog_Widget:
    def __init__(self, master):
        self.master = master
        self.master.title("Dog GUI")
      
        # Create two dog variables Buddy is 3 yrs old and Max is 3 yrs old
        self.dog_1 = Dog_Info("Buddy", 3)
        self.dog_2 = Dog_Info("Max", 5)

        # Tk Label () display doggos information text properties, bg color, 
        # text color, display name of  1st and 2nd dog also age using grid() widget
        tk.Label(self.master, font=("Comic Sans Ms", 15, "bold"),bg="lightpink", fg="gray"
                 ,text=f"Dog 1: {self.dog_1.name}, Age: 
                 {self.dog_1.age} years").grid(row=0, column=0, pady=10, padx=10)
        tk.Label(self.master, font=("Comic Sans Ms", 15, "bold"),
                 bg="lightpink", text=f"Dog 2: {self.dog_2.name}, 
                 Age: {self.dog_2.age} years").grid(row=1, column=0, pady=10, padx=10)

        # Button to make the oldest dog woof highlight bg
        button_woof = tk.Button(self.master, text="Make Oldest Dog Woof!"
                                ,highlightbackground="lightpink", command=self.oldest_dog_will_woof)
        # Using grid () widget for button
        button_woof.grid(row=2, column=0, pady=10, padx=10)
        
    # This is to show who is older using greater than to check their age 
    def oldest_dog_will_woof(self):
        oldest_dog = self.dog_1 if self.dog_1.age > self.dog_2.age else self.dog_2
        # The messagebox pop up will show the oldest dog name and will say woof woof
        messagebox.showinfo("Woof!", f"{oldest_dog.name} says: {oldest_dog.woof()}")

# Run tkinter mainloop ()
if __name__ == "__main__":
    root = tk.Tk()
    # Size of frame
    root.geometry("400x300")
    # Bg color of frame
    root.configure(bg="lightpink")
    Dog_Widget(root)
    root.mainloop()