import tkinter as tk
from tkinter import messagebox

def greet():
    messagebox.showinfo("Greetings", "Hello, Tkinter!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Click Me", command=greet)
button.pack(pady=10)

#create second button
button = tk.Button(root, text="CDAC BANGALORE",command=greet)
button.pack(pady=20)


# Run the Tkinter event loop
root.mainloop()
