import tkinter as tk
from tkinter import ttk

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("300x150")

        self.temperature_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        tk.Label(root, text="Enter Temperature:").pack(pady=10)
        entry_temp = tk.Entry(root, textvariable=self.temperature_var)
        entry_temp.pack(pady=5)

        tk.Label(root, text="Converted Temperature:").pack(pady=5)
        label_result = tk.Label(root, textvariable=self.result_var)
        label_result.pack(pady=10)

        convert_button = tk.Button(root, text="Convert", command=self.convert_temperature)
        convert_button.pack(pady=10)

        # Combobox for selecting conversion type
        self.conversion_type_var = tk.StringVar()
        self.conversion_type_var.set("C to F")  # Default conversion type
        self.conversion_combobox = ttk.Combobox(root, textvariable=self.conversion_type_var, values=["C to F", "F to C"])
        self.conversion_combobox.pack(pady=5)

    def convert_temperature(self):
        try:
            temperature = self.temperature_var.get()
            conversion_type = self.conversion_type_var.get()

            if conversion_type == "C to F":
                converted_temp = (temperature * 9/5) + 32
                self.result_var.set(f"{temperature:.2f}°C is {converted_temp:.2f}°F")
            elif conversion_type == "F to C":
                converted_temp = (temperature - 32) * 5/9
                self.result_var.set(f"{temperature:.2f}°F is {converted_temp:.2f}°C")
        except ValueError:
            self.result_var.set("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()