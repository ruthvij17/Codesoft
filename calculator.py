import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for the display
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place the buttons
row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(window, text=button, command=lambda b=button: entry.delete(0, tk.END)).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
window.mainloop()
