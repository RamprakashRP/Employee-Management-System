import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk


def promoteemployee():
    # Function to handle button clicks
    def promote_employee():
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="EmployeeDB"
        )

        cursor = db.cursor()

        # Get data from the entry fields
        employee_id = employee_id_entry.get()
        new_position = new_position_entry.get()
        new_salary = new_salary_entry.get()

        # Check if the new salary is greater than the current salary
        get_current_salary_query = "SELECT Salary FROM employee WHERE EmployeeID = %s"
        cursor.execute(get_current_salary_query, (employee_id,))
        current_salary = cursor.fetchone()

        if current_salary and new_salary > current_salary[0]:
            # Update employee's position and salary in the MySQL database
            update_query = "UPDATE employee SET Position = %s, Salary = %s WHERE EmployeeID = %s"
            data = (new_position, new_salary, employee_id)

            try:
                cursor.execute(update_query, data)
                db.commit()
                messagebox.showinfo("Success", "Employee promoted successfully!")
            except mysql.connector.Error as err:
                db.rollback()
                messagebox.showerror("Error", f"Failed to promote employee: {err}")
        else:
            messagebox.showerror("Error", "New salary must be greater than the current salary.")

        db.close()

    def cancel_promote_employee():
        promote_employee_window.destroy()

    promote_employee_window = tk.Tk()
    promote_employee_window.title("Employee Management System - Promote Employee")

    # Make the window full screen
    promote_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/promempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(promote_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/promempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 750
    frame_height = 500
    center_x = (promote_employee_window.winfo_screenwidth() - frame_width) // 2
    center_y = (promote_employee_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(promote_employee_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/promempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for employee information
    employee_id_label = tk.Label(frame, text="Employee ID :", font=("Arial", 16))
    employee_id_label.place(x=150, y=150)
    employee_id_entry = tk.Entry(frame, font=("Arial", 14))
    employee_id_entry.place(x=315, y=150, relwidth=0.4)

    new_position_label = tk.Label(frame, text="New Position:", font=("Arial", 16))
    new_position_label.place(x=150, y=225)
    new_position_entry = tk.Entry(frame, font=("Arial", 14))
    new_position_entry.place(x=315, y=225, relwidth=0.4)

    new_salary_label = tk.Label(frame, text=" New Salary  :", font=("Arial", 16))
    new_salary_label.place(x=150, y=300)
    new_salary_entry = tk.Entry(frame, font=("Arial", 14))
    new_salary_entry.place(x=315, y=300, relwidth=0.4)

    # Create the Promote Employee button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=promote_employee,
        font=("Arial", 16),
        fg="white",
        image=submit_button_bg_photo,
        compound=tk.CENTER,
        borderwidth=0,
    )

    submit_button.image = submit_button_bg_photo
    submit_button.hover_image = submit_button_hover_bg_photo

    submit_button.place(x=175, y=400, width=150, height=50)

    # Create the Cancel button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        frame,
        text="Cancel",
        command=cancel_promote_employee,
        font=("Arial", 16),
        fg="white",
        image=cancel_button_bg_photo,
        compound=tk.CENTER,
        borderwidth=0,
    )

    cancel_button.image = cancel_button_bg_photo
    cancel_button.hover_image = cancel_button_hover_bg_photo

    cancel_button.place(x=400, y=400, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the buttons for hover effect
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    promote_employee_window.mainloop()
