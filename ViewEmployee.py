import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk


def viewemloyee():
    # Function to set alternating row colors
    def set_alternating_row_colors(treeview, odd_color, even_color):
        for i, item in enumerate(treeview.get_children()):
            if i % 2 == 0:
                treeview.item(item, tags=("even",))
                treeview.tag_configure("even", background=even_color)
            else:
                treeview.item(item, tags=("odd",))
                treeview.tag_configure("odd", background=odd_color)

    # Function to fetch employee data from the database
    def fetch_employee_data():
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()
        cursor.execute("SELECT EmployeeID, Name, Email, MobNo, Position, Salary FROM employee")

        employee_data = cursor.fetchall()

        cursor.execute("SELECT ManagerID, Name, Email, MobNo, Position, Salary FROM manager")

        manager_data = cursor.fetchall()

        employee_data = manager_data + employee_data

        db.close()

        return employee_data

    # Create the "View Employee" window
    view_employee_window = tk.Tk()
    view_employee_window.title("Employee Management System - View Employees")

    # Make the window full screen
    view_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/viewempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(view_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/viewempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 1100
    frame_height = 600
    center_x = (view_employee_window.winfo_screenwidth() - frame_width) // 2
    center_y = (view_employee_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(view_employee_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/viewempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create a Treeview widget to display employee data
    columns = ("Employee ID", "Name", "Email", "MobNo", "Position", "Salary")
    treeview = ttk.Treeview(frame, columns=columns, show="headings")

    # Configure column headings
    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=175)  # Adjust column width as needed

    # Fetch data from the database
    employee_data = fetch_employee_data()

    # Insert data into the Treeview
    for data in employee_data:
        treeview.insert("", "end", values=data)

    # Set alternating row colors (customize colors here)
    odd_row_color = "lightgray"
    even_row_color = "lightblue"
    set_alternating_row_colors(treeview, odd_row_color, even_row_color)

    # Place the Treeview widget at the center of the frame
    treeview.place(x=25, y=100, height=475)

    # Start the GUI main loop
    view_employee_window.mainloop()
