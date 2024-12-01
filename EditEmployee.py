import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk


def editemployee():
    # Function to fetch employee details from the database
    def fetch_employee_details(employee_id):
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()
        query = "SELECT * FROM employee WHERE EmployeeID = %s"
        cursor.execute(query, (employee_id,))
        employee_data = cursor.fetchone()

        db.close()

        return employee_data

    # Function to update employee details in the database
    def update_employee_details(employee_id, name, email, mobno):
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()
        update_query = "UPDATE employee SET Name = %s, Email = %s, MobNo = %s WHERE EmployeeID = %s"
        data = (name, email, mobno, employee_id)

        try:
            cursor.execute(update_query, data)
            db.commit()
            return True
        except mysql.connector.Error as err:
            db.rollback()
            return False
        finally:
            db.close()

    # Function to handle the "Save" button click
    def save_changes():
        employee_id = employee_id_label.cget("text")
        name = name_entry.get()
        email = email_entry.get()
        mobno = mobno_entry.get()

        if update_employee_details(employee_id, name, email, mobno):
            messagebox.showinfo("Success", "Details updated successfully!")
        else:
            messagebox.showerror("Error", "Failed to update details. Please try again.")

    # Create the "Edit Details" window
    edit_employee_window = tk.Tk()
    edit_employee_window.title("Employee Management System - Edit Employee")

    # Make the window full screen
    edit_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/editempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(edit_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/editempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 750
    frame_height = 500
    center_x = (edit_employee_window.winfo_screenwidth() - frame_width) // 2
    center_y = (edit_employee_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(edit_employee_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/editempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Fetch employee details based on the current employee ID (replace with your logic)
    employee_id = "emp01"  # Replace with the actual employee ID

    employee_data = fetch_employee_details(employee_id)

    # Create labels and entry fields for employee details
    employee_id_label = tk.Label(frame, text="Employee ID:", font=("Arial", 14))
    employee_id_label.place(x=150, y=150)
    employee_entry = tk.Entry(frame, font=("Arial", 14))
    employee_entry.insert(0, employee_data[0])
    employee_entry.place(x=315, y=150, relwidth=0.4)

    name_label = tk.Label(frame, text="Name:", font=("Arial", 16))
    name_label.place(x=150, y=200)
    name_entry = tk.Entry(frame, font=("Arial", 14))
    name_entry.insert(0, employee_data[1])
    name_entry.place(x=315, y=200, relwidth=0.4)

    email_label = tk.Label(frame, text="Email:", font=("Arial", 16))
    email_label.place(x=150, y=250)
    email_entry = tk.Entry(frame, font=("Arial", 14))
    email_entry.insert(0, employee_data[2])
    email_entry.place(x=315, y=250, relwidth=0.4)

    mobno_label = tk.Label(frame, text="Mobile No:", font=("Arial", 16))
    mobno_label.place(x=150, y=300)
    mobno_entry = tk.Entry(frame, font=("Arial", 14))
    mobno_entry.insert(0, employee_data[3])
    mobno_entry.place(x=315, y=300, relwidth=0.4)

    # ... (Previous code)

    # Create the "Save" button
    save_button_bg = Image.open("res/#0000FF.png")
    save_button_bg_photo = ImageTk.PhotoImage(save_button_bg)
    save_button_hover_bg = Image.open("res/#007FFF.png")
    save_button_hover_bg_photo = ImageTk.PhotoImage(save_button_hover_bg)

    save_button = tk.Button(
        frame,
        text="Save",
        command=save_changes,
        font=("Arial", 16),
        fg="white",
        image=save_button_bg_photo,
        compound=tk.CENTER,
        borderwidth=0,
    )

    save_button.image = save_button_bg_photo
    save_button.hover_image = save_button_hover_bg_photo

    save_button.place(x=150, y=400, width=150, height=50)

    # Create the "Cancel" button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        frame,
        text="Cancel",
        command=edit_employee_window.destroy,
        font=("Arial", 16),
        fg="white",
        image=cancel_button_bg_photo,
        compound=tk.CENTER,
        borderwidth=0,
    )

    cancel_button.image = cancel_button_bg_photo
    cancel_button.hover_image = cancel_button_hover_bg_photo

    cancel_button.place(x=450, y=400, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the "Save" button for hover effect
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    # Start the GUI main loop
    edit_employee_window.mainloop()
