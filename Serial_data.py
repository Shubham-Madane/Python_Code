import tkinter as tk
import serial
from tkinter import messagebox
#import serial

def process_data():
    values = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get()]
    print("Entered Values:", values)        
    # You can store the entered values in a variable, write them to a file, or store them in a database
  
    # Convert the array into a single string
    data_string = ''.join(values)
    # Print the result
    print(data_string)


# Configure serial port
ser = serial.Serial('COM1', 9600)  # Change 'COM1' to your port and 9600 to your baud rate


# Function to read data from serial port and send it back
def echo_serial_data():
    try:
        while True:
            # Read data from serial port
            data = ser.readline().decode().strip()
            print("Received data:", data)
              # Update label with received data
            label.config(text=data)
            # Send the received data back
            ser.write(data.encode())
            ser.flush()  # Ensure data is sent immediately
    except serial.SerialException as e:
        print("Error:", e)
        label.config(text="Error: Serial port not available")


def display_message():
    messagebox.showinfo(" Alert ", "Data Updated....!")

# Create the main application window
root = tk.Tk()
root.title(" Battery Monitoring System GUI ")

# Change background color
#root.configure(bg="light blue")  # Change "light blue" to the desired color

# Create a frame to contain widgets
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=2, pady=5)
frame.pack(padx=100, pady=100)

# Load the image
##logo_image = tk.PhotoImage(file="E:\Python\Test1_BMS\image\logo_cdac_round.png")  # Change "logo.png" to the path of your logo image
# Resize the image
##logo_image = logo_image.subsample(3, 3)  # Change the subsample factors as needed to resize the image

# Create a label to display the logo
##logo_label_1 = tk.Label(root, image=logo_image)
#logo_label.grid(row=20, column=0, columnspan=3, pady=10)
#logo_label.pack()

##logo_label_1.place(x=10, y=10)  # Adjust x and y coordinates as needed

# Load the image
##logo_image1 = tk.PhotoImage(file="E:\Python\Test1_BMS\image\picture.png")  # Change "logo.png" to the path of your logo image
# Resize the image
##logo_image1 = logo_image1.subsample(10, 10)  # Change the subsample factors as needed to resize the image

# Create a label to display the logo
##logo_label1 = tk.Label(root, image=logo_image1)
#logo_label.grid(row=20, column=0, columnspan=3, pady=10)
#logo_label.pack()

##logo_label1.place(x=450, y=10)  # Adjust x and y coordinates as needed



# Create a label widget
label = tk.Label(frame, text="Welcome Shubham ", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=10)

# Create an entry widget
#label = tk.Label(frame, text="user", font=("Helvetica", 10))
#label.grid(row=1, column=0, columnspan=2, pady=5)
#entry = tk.Entry(frame)
#entry.grid(row=1, column=1, columnspan=2, pady=5)

# Create a second button widget
exit_button = tk.Button(frame, text="Consumer", font=("Helvetica", 10))
exit_button.grid(row=1, column=1, pady=20)


def display_selected_option(selected_option):
    messagebox.showinfo("Selected Option", f"You selected: {selected_option}")


# Define the options for the dropdown menu
options = ["Single Battery", "Multiple Battery"]

# Create a variable to hold the selected option
selected_option = tk.StringVar(root)
selected_option.set("Select...")  # Set the default option

# Create the dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *options, command=display_selected_option)
#dropdown.grid(row=4, column=1, pady=10)
dropdown.place(x=200, y=40)  # Adjust these coordinates to position the dropdown
#dropdown.pack(pady=20)


# Create an Variable 1
label = tk.Label(frame, text="No of Battery :", font=("Helvetica", 10))
label.grid(row=5, column=0, columnspan=1, pady=5)
var1 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var1)
entry.grid(row=5, column=1, columnspan=2, pady=5)
#print("No of Battery:  ",entry)
#entry.pack()

# Create a button to process the entered data
button = tk.Button(frame, text="Process Data", command=process_data)
#process_button.pack(pady=10)


# Create an Variable 2
label = tk.Label(frame, text="Total Voltage :", font=("Helvetica", 10))
label.grid(row=6, column=0, columnspan=1, pady=5)
var2 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var2)
entry.grid(row=6, column=1, columnspan=2, pady=5)
print("Total Voltage:  ",entry)

# Create an Variable 3
label = tk.Label(frame, text="Battery_high_voltage :", font=("Helvetica", 10))
label.grid(row=7, column=0, columnspan=1, pady=5)
var3 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var3)
entry.grid(row=7, column=1, columnspan=2, pady=5)

# Create an Variable 4
label = tk.Label(frame, text="Battery_low_voltage :", font=("Helvetica", 10))
label.grid(row=8, column=0, columnspan=1, pady=5)
var4 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var4)
entry.grid(row=8, column=1, columnspan=2, pady=5)

# Create an Variable 5
label = tk.Label(frame, text="Battery_low_Temp :", font=("Helvetica", 10))
label.grid(row=9, column=0, columnspan=1, pady=5)
var5 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var5)
entry.grid(row=9, column=1, columnspan=2, pady=5)

# Create an Variable 6
label = tk.Label(frame, text="current_high :", font=("Helvetica", 10))
label.grid(row=10, column=0, columnspan=1, pady=5)
var6 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var6)
entry.grid(row=10, column=1, columnspan=2, pady=5)

# Create an Variable 7
label = tk.Label(frame, text="Offset Value :", font=("Helvetica", 10))
label.grid(row=11, column=0, columnspan=1, pady=5)
var7 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var7)
entry.grid(row=11, column=1, columnspan=2, pady=5)

# Create an Variable 8
label = tk.Label(frame, text="sensitivity   :", font=("Helvetica", 10))
label.grid(row=12, column=0, columnspan=1, pady=5)
var8 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var8)
entry.grid(row=12, column=1, columnspan=2, pady=5)

# Create an Variable 9
label = tk.Label(frame, text="Total Capacity :", font=("Helvetica", 10))
label.grid(row=13, column=0, columnspan=1, pady=5)
var9 = tk.StringVar(frame)
entry = tk.Entry(frame,textvariable=var9)
entry.grid(row=13, column=1, columnspan=2, pady=5)

# Create an entry widget
#entry = tk.Entry(frame)
#entry.grid(row=1, column=0, columnspan=2, pady=5)

# Create a button widget for show the text box
button = tk.Button(frame, text="Save Me!", command=display_message,  width=15)
button.grid(row=16, column=1, pady=10)
#button.pack(pady=10)


# Create a button to process the entered data and it will the print the data in terminal
process_button = tk.Button(frame,text="Process Data", command=process_data,  width=15)
#process_button.pack(pady=100)
process_button.grid(row=16, column=2, pady=20)


# Create a Exit button widget it will close the GUI
exit_button = tk.Button(frame, text="Exit", command=root.quit, width=15)
exit_button.grid(row=17, column=1, pady=20)
#exit_button.pack(pady=80)

# Call the function to start reading and echoing serial data
echo_serial_data()

# Run the Tkinter event loop
root.mainloop()










