import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task List
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
task_list.pack(pady=10)

# Remove Task Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Start the GUI
root.mainloop()
