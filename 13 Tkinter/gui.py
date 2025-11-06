import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")  # width x height

# Add a label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=10)

# Add an entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Function to display a message
def show_message():
    user_text = entry.get()
    label.config(text=f"Hello, {user_text}!")

# Add a button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=10)

# Run the GUI loop
root.mainloop()
