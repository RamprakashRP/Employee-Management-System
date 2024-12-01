import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

def addemployee():
    # Function to handle button clicks
    def add_employee():
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()

        # Get data from the entry fields
        employee_id = employee_id_entry.get()
        name = name_entry.get()
        position = position_entry.get()
        salary = salary_entry.get()
        mobno = mobno_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        # Insert employee data into the MySQL database
        insert_query = "INSERT INTO employee (EmployeeID, Name, Position, Salary, MobNo, Email, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (employee_id, name, position, salary, mobno, email, password)

        try:
            cursor.execute(insert_query, data)
            db.commit()
            messagebox.showinfo("Success", "Employee added successfully!")
        except mysql.connector.Error as err:
            db.rollback()
            messagebox.showerror("Error", f"Failed to add employee: {err}")

        db.close()

    def cancel_add_employee():
        add_employee_window.destroy()

    add_employee_window = tk.Tk()
    add_employee_window.title("Employee Management System - Add Employee")

    # Make the window full screen
    add_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/addempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(add_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame = tk.Frame(add_employee_window, bd=5, relief=tk.SUNKEN)
    frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.6, anchor="center")

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/addempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for employee information
    employee_id_label = tk.Label(frame, text="Employee ID:", font=("Arial", 16))
    employee_id_label.place(x=150, y=75)
    employee_id_entry = tk.Entry(frame, font=("Arial", 14))
    employee_id_entry.place(x=300, y=75, relwidth=0.4)

    name_label = tk.Label(frame, text="      Name     :", font=("Arial", 16))
    name_label.place(x=150, y=125)
    name_entry = tk.Entry(frame, font=("Arial", 14))
    name_entry.place(x=300, y=125, relwidth=0.4)

    position_label = tk.Label(frame, text="    Position   :", font=("Arial", 16))
    position_label.place(x=150, y=175)
    position_entry = tk.Entry(frame, font=("Arial", 14))
    position_entry.place(x=300, y=175, relwidth=0.4)

    salary_label = tk.Label(frame, text="     Salary     :", font=("Arial", 16))
    salary_label.place(x=150, y=225)
    salary_entry = tk.Entry(frame, font=("Arial", 14))
    salary_entry.place(x=300, y=225, relwidth=0.4)

    mobno_label = tk.Label(frame, text="  Mobile No   :", font=("Arial", 16))
    mobno_label.place(x=150, y=275)
    mobno_entry = tk.Entry(frame, font=("Arial", 14))
    mobno_entry.place(x=300, y=275, relwidth=0.4)

    email_label = tk.Label(frame, text="      Email      :", font=("Arial", 16))
    email_label.place(x=150, y=325)
    email_entry = tk.Entry(frame, font=("Arial", 14))
    email_entry.place(x=300, y=325, relwidth=0.4)

    password_label = tk.Label(frame, text="   Password  :", font=("Arial", 16))
    password_label.place(x=150, y=375)
    password_entry = tk.Entry(frame, show="*", font=("Arial", 14))
    password_entry.place(x=300, y=375, relwidth=0.4)

    # Create the Add Employee button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=add_employee,
        font=("Arial", 16),
        fg="white",
        bg="blue",
        borderwidth=0,
        image=submit_button_bg_photo,
        compound=tk.CENTER
    )

    submit_button.image = submit_button_bg_photo
    submit_button.hover_image = submit_button_hover_bg_photo

    submit_button.place(x=250, y=435, width=150, height=50)

    # Create the Add Employee button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    # Create the Cancel button
    cancel_button = tk.Button(
        frame,
        text="Cancel",
        command=cancel_add_employee,
        font=("Arial", 16),
        fg="white",
        bg="red",
        borderwidth=0,
        image=cancel_button_bg_photo,
        compound=tk.CENTER
    )

    cancel_button.image = cancel_button_bg_photo
    cancel_button.hover_image = cancel_button_hover_bg_photo

    cancel_button.place(x=450, y=435, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the "Submit" button for hover effect
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    add_employee_window.mainloop()

addemployee()