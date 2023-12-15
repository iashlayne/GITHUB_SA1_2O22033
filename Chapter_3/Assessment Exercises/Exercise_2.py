# Exercise 3 - Vending Machine

import tkinter as tk
from tkinter import messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Variables to store user selections
        self.coffee_type = tk.StringVar()
        self.sugar_level = tk.IntVar()
        self.milk_option = tk.BooleanVar()
        self.money_inserted = tk.DoubleVar(value=0.0)

        # Configure background color
        self.root.configure(bg="#D2B48C")

        # Create coffee type options
        coffee_types = ["Espresso", "Latte", "Cappuccino"]

        for coffee_type in coffee_types:
            button = tk.Radiobutton(root, text=coffee_type, variable=self.coffee_type, value=coffee_type, indicatoron=0,
                                    width=20, height=2, bd=4, bg="#8B4513", fg="white",
                                    activebackground="#A52A2A")
            button.pack(pady=5)

        # Create sugar level option
        tk.Label(root, text="Sugar Level:", bg="#D2B48C", fg="#8B4513").pack()
        tk.Scale(root, from_=0, to=5, orient="horizontal", variable=self.sugar_level, bg="#8B4513",
                 fg="white", highlightbackground="#A52A2A", sliderlength=15, length=150).pack()

        # Create milk option
        tk.Checkbutton(root, text="Add Milk", variable=self.milk_option, bg="#D2B48C", fg="#8B4513").pack()

        # Create money entry
        tk.Label(root, text="Insert Money ($):", bg="#D2B48C", fg="#8B4513").pack()
        tk.Entry(root, textvariable=self.money_inserted, width=10, bg="#8B4513", fg="white").pack()

        # Create buy button
        tk.Button(root, text="Buy Coffee", command=self.buy_coffee, bg="#D2B48C",highlightbackground="#D2B48C").pack(pady=10)

    def buy_coffee(self):
        # Calculate the cost of the selected coffee
        coffee_price = self.calculate_coffee_price()
        
        # Check if the money is sufficient
        if self.money_inserted.get() >= coffee_price:
            # Display user selections and change using a messagebox
            change = self.money_inserted.get() - coffee_price
            message = f"Selected Coffee: {self.coffee_type.get()}\nSugar Level: {self.sugar_level.get()}\n"
            message += f"Milk Added: {'Yes' if self.milk_option.get() else 'No'}\n"
            message += f"Cost: ${coffee_price:.2f}\nMoney Inserted: ${self.money_inserted.get():.2f}\nChange: ${change:.2f}"
            messagebox.showinfo("Order Summary", message)
        else:
            messagebox.showwarning("Insufficient Funds", "Please insert enough money to buy the selected coffee.")

    def calculate_coffee_price(self):
        # Simple cost calculation (replace with your actual pricing logic)
        base_price = 2.50
        sugar_cost = 0.25 * self.sugar_level.get()
        milk_cost = 0.50 if self.milk_option.get() else 0.0
        return base_price + sugar_cost + milk_cost

if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = CoffeeVendingMachine(root)
    root.mainloop()