import tkinter as tk
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
window = tk.Tk()
window.title("Simple Calculator")
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
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
window.mainloop()
