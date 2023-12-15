# EXERICSE 1 - GREETING APP
import tkinter as tk
from tkinter import ttk

# Class "GreetingApp" to call it later on 
class GreetingApp:
    # Define a method using app to be called later on and window to be use for the window properties
    def __init__(app, window):
        app.window = window
        # Greeting title
        app.window.title("Greeting App")
        # Size of the shown frame when code is running
        app.window.geometry("700x500")
        
        # Input_frame - Left side of the frame in white background
        app.input_frame = tk.Frame(window, bg="white")
        app.input_frame.pack(side="left", fill="both", expand=True)
    
        # Display_frame - Right side of the frame in white background
        app.display_frame = tk.Frame(window, bg="black")
        app.display_frame.pack(side="right", fill="both", expand=True)
        
        # Call to function creating widgets  in Input Frame and Display Frame
        app.InputFrame()
        app.DisplayFrame()
    
    # Defined a method InputFrame()
    def InputFrame(app):
        # Title label in Input frame with comic sans font style, white bg, and blue text fg=""
        title_label = tk.Label(app.input_frame, text="Greeting App", font=("Comic Sans MS", 
                                                      18, "bold" ), bg="white", fg="blue")
        
        # GREETING APP 
        # positioning of the word "GREETING APP" in grid manner
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # ▬ USER ENTRY: NAME
        # Entry of widget of the user's name with gray background
        app.name_enter = tk.Entry(app.input_frame, width=20, bg="gray")
        app.name_enter.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        
        # Label for selection of user choice of color in Inputframe with white Background 
        color_select = tk.Label(app.input_frame, text="Please Select Color:", bg="white", fg="black")
        
        # Please Select Color:
        # positioning of the word "Please Select Color:" in grid manner
        color_select.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        
        # Using class () String Var for the color selection container
        app.color = tk.StringVar()
        # setting initialize to white when frame is opened
        app.color.set("white")
        
        # Combobox for color selection with the available light colors
        color_choices = ["lightpink", "lightsalmon", "lightyellow", "lightblue", "lightgreen", "plum"]
        app.color_selection = ttk.Combobox(app.input_frame, 
                                           textvariable=app.color, values=color_choices)
        
        # "lightpink", "lightsalmon", "lightyellow", "lightblue", "lightgreen", "plum" 
        # positioning of the word these colors ^^^^ in grid manner
        app.color_selection.grid(row=3, column=0, columnspan=2, pady=10)
        
        # BUTTON for when user click the button it will display on the right side of the frame 
        # the Greeting.
        update_button = tk.Button(app.input_frame, text="Update Greeting", 
                                  command=app.update_greet, highlightbackground="white")
        
        # Update Greeting - button 𓋰
        # positioning of the button Update Greeting in grid manner
        update_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Defined a method DisplayFrame()
    def DisplayFrame(app):
        # Label to show the personalized greeting to the user in font comic sans ms font size 15 
        # and bg color black
        app.greet_user = tk.Label(app.display_frame, text="", font=("Comic Sans MS", 15),bg="black")
        # Position of the greeting on display frame using pady= y (50) axis padding
        app.greet_user.pack(pady=50)
    
    # Defined a method update_greet()
    def update_greet(app):
        # To get user's name and the color choice
        user_name = app.name_enter.get()
        color_pick = app.color.get()
        
        # Displayed text ""Hey There, {user_name}!, Have a nice day!" with user's name and 
        # color selected
        greet_text = f"Hey There, {user_name}!, Have a nice day!"
        app.greet_user.config(text=greet_text, fg=color_pick)
  
# # To run the Tkinter event loop
if __name__ == "__main__":
    window = tk.Tk()
    GreetingApp(window)
    window.mainloop()
        