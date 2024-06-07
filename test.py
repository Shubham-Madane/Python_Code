import tkinter as tk
import serial

def read_serial_data():
    try:
        # Open serial port
        ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the appropriate port name
        while True:
            # Read data from serial port
            data = ser.readline().decode().strip()
            print("Received data:", data)
            # Update label with received data
            label.config(text=data)
            # Update GUI
            root.update_idletasks()
    except serial.SerialException as e:
        print("Error:", e)
        label.config(text="Error: Serial port not available")

# Create the main application window
root = tk.Tk()
root.title("Serial Data Reader")

# Create a label to display the received data
label = tk.Label(root, text="Waiting for serial data...")
label.pack()

# Start reading serial data
read_serial_data()

# Run the Tkinter event loop
root.mainloop()
