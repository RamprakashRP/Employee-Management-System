import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from mainmenu import managermm, chairmanmm

def Login():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        if ("emp" in username):
            cursor = db.cursor()
            cursor.execute("SELECT * FROM employee WHERE EmployeeID = %s", (username,))
            user = cursor.fetchone()

            if user:
                if user[6] == password:  # Index 6 corresponds to the Password column in the users table
                    login_window.destroy()
                    print("Success")

                else:
                    messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror("Error", "User not found")

        elif ("mgr" in username):
            cursor = db.cursor()
            cursor.execute("SELECT * FROM manager WHERE ManagerID = %s", (username,))
            user = cursor.fetchone()

            if user:
                if user[6] == password:  # Index 6 corresponds to the Password column in the users table
                    login_window.destroy()
                    managermm()
                else:
                    messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror("Error", "User not found")

        elif ("chrmn" in username):
            cursor = db.cursor()
            cursor.execute("SELECT * FROM manager WHERE ManagerID = %s", (username,))
            user = cursor.fetchone()

            if user:
                if user[6] == password:  # Index 6 corresponds to the Password column in the users table
                    login_window.destroy()
                    chairmanmm()
                else:
                    messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror("Error", "User not found")

        else:
            messagebox.showerror("Error", "Enter Proper Username")

    login_window = tk.Tk()
    login_window.title("Employee Management System - Login")

    # Make the window full screen
    login_window.attributes("-fullscreen", True)

    # Set the window size to 1920 x 1080 pixels
    login_window.geometry("1920x1080")

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/loginbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(login_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame = tk.Frame(login_window, bd=5, relief=tk.SUNKEN)
    frame.place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.45, anchor="center")

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/loginol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create the Username Label
    username_label = tk.Label(frame, text="Employee ID :", font=("Arial", 16), fg="blue", bg="black")
    username_label.place(x=100, y=140)

    # Create the Username Entry
    username_entry = tk.Entry(frame, font=("Arial", 14))
    username_entry.place(x=250, y=140, relwidth=0.4)

    # Create the Password Label
    password_label = tk.Label(frame, text="  Password   :", font=("Arial", 16), fg="red", bg="black")
    password_label.place(x=100, y=210)

    # Create the Password Entry
    password_entry = tk.Entry(frame, show="*", font=("Arial", 14))
    password_entry.place(x=250, y=210, relwidth=0.4)

    # Create a frame with a white background as the outline for the button
    login_button_frame = tk.Frame(frame, bg="white")
    login_button_frame.place(x=155, y=300, relwidth=0.5, height=40)

    def on_enter(event):
        login_button.config(image=hover_gradient_image)

    def on_leave(event):
        login_button.config(image=gradient_image)

    # Load the gradient image and the hover gradient image
    gradient_image = Image.open("res/#062e08.png")
    gradient_image = ImageTk.PhotoImage(gradient_image)

    hover_gradient_image = Image.open("res/#1B8220.png")
    hover_gradient_image = ImageTk.PhotoImage(hover_gradient_image)

    # Create the Login Button inside the frame
    login_button = tk.Button(
        login_button_frame,
        text="Login",
        command=login,
        font=("Arial", 16),
        fg="white",
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    login_button.image = gradient_image
    login_button.hover_image = hover_gradient_image

    login_button.place(relwidth=1, relheight=1)

    # Bind mouse events to the button
    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)

    login_window.mainloop()

