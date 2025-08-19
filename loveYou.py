# import tkinter as tk
# from tkinter import messagebox
#
# def yes_clicked():
#     messagebox.showinfo("Response", "I knew it ❤️")
#
# def no_clicked():
#     messagebox.showinfo("Response", "You can’t say no to me 😏")
#
# root = tk.Tk()
# root.title("Do you love me?")
# root.geometry("300x200")
#
# label = tk.Label(root, text="Do you love me?", font=("Arial", 14))
# label.pack(pady=20)
#
# yes_button = tk.Button(root, text="Yes", command=yes_clicked)
# yes_button.pack(side="left", padx=40, pady=20)
#
# no_button = tk.Button(root, text="No", command=no_clicked)
# no_button.pack(side="right", padx=40, pady=20)
#
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import random
#
# def yes_clicked():
#     messagebox.showinfo("Answer", "Kya?? pahle shakal dekh Apni 😒😒 ")
#
# def move_no_button(event):
#     # Get window size
#     win_width = root.winfo_width()
#     win_height = root.winfo_height()
#
#     # Random new position
#     new_x = random.randint(0, win_width - no_button.winfo_width())
#     new_y = random.randint(0, win_height - no_button.winfo_height())
#
#     no_button.place(x=new_x, y=new_y)
#
# # Create main window
# root = tk.Tk()
# root.title("Do you love me?")
# root.geometry("500x400")
# root.configure(bg="pink")
#
# # Label
# label = tk.Label(root, text="Do you love me?", font=("Arial", 20, "bold"), bg="pink")
# label.pack(pady=50)
#
# # Yes button
# yes_button = tk.Button(root, text="Yes", font=("Arial", 14), bg="green", fg="white", command=yes_clicked)
# yes_button.place(x=150, y=200)
#
# # No button
# no_button = tk.Button(root, text="No", font=("Arial", 14), bg="red", fg="white")
# no_button.place(x=250, y=200)
#
# # Bind hover event to No button
# no_button.bind("<Enter>", move_no_button)
#
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random

def yes_clicked():
    messagebox.showinfo("Answer", "Kya?? pahle shakal dekh Apni 😒😒 ")

def move_no_button(event):
    # Get window size
    win_width = root.winfo_width()
    win_height = root.winfo_height()

    # Random new position
    new_x = random.randint(0, win_width - no_button.winfo_width())
    new_y = random.randint(0, win_height - no_button.winfo_height())

    no_button.place(x=new_x, y=new_y)

# Create main window
root = tk.Tk()
root.title("Do you love me?")
root.geometry("500x500")
root.configure(bg="pink")

# Load an image (GIF or PNG)
# Make sure "proposal.png" exists in the same folder
proposal_img = tk.PhotoImage(file="img.gif")

# Display image at top
img_label = tk.Label(root, image=proposal_img, bg="pink")
img_label.pack(pady=(10, 5))

# Question label
label = tk.Label(root, text="Do you love me?", font=("Arial", 20, "bold"), bg="pink")
label.pack(pady=(0, 40))

# Yes button
yes_button = tk.Button(root, text="Yes", font=("Arial", 14), bg="green", fg="white", command=yes_clicked)
yes_button.place(x=150, y=350)

# No button
no_button = tk.Button(root, text="No", font=("Arial", 14), bg="red", fg="white")
no_button.place(x=250, y=350)

# Bind hover event to No button
no_button.bind("<Enter>", move_no_button)

root.mainloop()
