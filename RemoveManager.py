import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk


def removemanager():
    # Function to handle button clicks
    def remove_manager():
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()

        # Get data from the entry fields
        manager_id = manager_id_entry.get()
        mobno = mobno_entry.get()

        # Check if the manager exists
        check_query = "SELECT * FROM manager WHERE ManagerID = %s AND MobNo = %s"
        data = (manager_id, mobno)

        cursor.execute(check_query, data)
        manager = cursor.fetchone()

        if manager:
            # Manager exists, proceed with removal
            remove_query = "DELETE FROM manager WHERE ManagerID = %s AND MobNo = %s"
            cursor.execute(remove_query, data)
            db.commit()
            messagebox.showinfo("Success", "Manager removed successfully!")
        else:
            # Manager does not exist
            messagebox.showerror("Error", "Manager not found. Please check the Manager ID and Mobile No.")

        db.close()

    def cancel_remove_manager():
        remove_manager_window.destroy()

    remove_manager_window = tk.Tk()
    remove_manager_window.title("Manager Management System - Remove Manager")

    # Make the window full screen
    remove_manager_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/remempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(remove_manager_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/remempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 750
    frame_height = 500
    center_x = (remove_manager_window.winfo_screenwidth() - frame_width) // 2
    center_y = (remove_manager_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(remove_manager_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/remempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for manager information
    manager_id_label = tk.Label(frame, text="Manager ID:", font=("Arial", 16))
    manager_id_label.place(x=150, y=200)
    manager_id_entry = tk.Entry(frame, font=("Arial", 14))
    manager_id_entry.place(x=300, y=200, relwidth=0.4)

    mobno_label = tk.Label(frame, text="  Mobile No  :", font=("Arial", 16))
    mobno_label.place(x=150, y=275)
    mobno_entry = tk.Entry(frame, font=("Arial", 14))
    mobno_entry.place(x=300, y=275, relwidth=0.4)

    # Create the Remove Manager button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=remove_manager,
        font=("Arial", 16),
        fg="white",
        image=submit_button_bg_photo,
        compound=tk.CENTER,
        borderwidth=0,
    )

    submit_button.image = submit_button_bg_photo
    submit_button.hover_image = submit_button_hover_bg_photo

    submit_button.place(x=150, y=400, width=150, height=50)

    # Create the Cancel button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        frame,
        text="Cancel",
        command=cancel_remove_manager,
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

    # Bind mouse events to the buttons for hover effect
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    remove_manager_window.mainloop()
