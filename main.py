import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk

curuser = None

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


def managermm(curid="mgr01"):

    curuser = "Manager"

    # Function to handle button clicks
    def button_click(button_name):
        # Replace this with the actions you want to perform when each button is clicked
        messagebox.showinfo("Button Clicked", f"You clicked the {button_name} button.")

    def cancel_remove_manager():
        main_menu_window.destroy()
        Login()

    main_menu_window = tk.Tk()
    main_menu_window.title("Employee Management System - Main Menu")

    # Make the window full screen
    main_menu_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open(
        "res/mainmenubg.png")  # Replace with your image path
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(main_menu_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame = tk.Frame(main_menu_window, bd=5, relief=tk.SUNKEN)
    frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.6, anchor="center")

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/mainmenuol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Load the gradient image and the hover gradient image
    gradient_image = Image.open(
        "res/#AA0000.png")  # Replace with your gradient image path
    gradient_image = ImageTk.PhotoImage(gradient_image)

    hover_gradient_image = Image.open(
        "res/#CC0000.png")  # Replace with your hover gradient image path
    hover_gradient_image = ImageTk.PhotoImage(hover_gradient_image)

    # Customizations for each button
    customizations = [
        {"text": "Add Employee", "fg": "black"},
        {"text": "Remove Employee", "fg": "black"},
        {"text": "Promote Employee", "fg": "black"},
        {"text": "Demote Employee", "fg": "black"},
        {"text": "View Employee", "fg": "black"},
        {"text": "Edit Employee", "fg": "black"}
    ]

    def addempmm():
        main_menu_window.destroy()
        addemployee(curuser)

    button_1 = tk.Button(
        frame,
        text=customizations[0]["text"],
        command=addempmm,
        font=("Arial", 16),
        fg=customizations[0]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_1.image = gradient_image
    button_1.hover_image = hover_gradient_image

    def remempmm():
        main_menu_window.destroy()
        removeemployee(curuser)

    button_2 = tk.Button(
        frame,
        text=customizations[1]["text"],
        command=remempmm,
        font=("Arial", 16),
        fg=customizations[1]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_2.image = gradient_image
    button_2.hover_image = hover_gradient_image

    def promempmm():
        main_menu_window.destroy()
        promoteemployee(curuser)

    button_3 = tk.Button(
        frame,
        text=customizations[2]["text"],
        command=promempmm,
        font=("Arial", 16),
        fg=customizations[2]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Continue creating buttons for each option
    button_3.image = gradient_image
    button_3.hover_image = hover_gradient_image

    def demempmm():
        main_menu_window.destroy()
        demoteemployee(curuser)

    button_4 = tk.Button(
        frame,
        text=customizations[3]["text"],
        command=demempmm,
        font=("Arial", 16),
        fg=customizations[3]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_4.image = gradient_image
    button_4.hover_image = hover_gradient_image

    def viewempmm():
        main_menu_window.destroy()
        viewemployee(curuser)

    button_5 = tk.Button(
        frame,
        text=customizations[4]["text"],
        command=viewempmm,
        font=("Arial", 16),
        fg=customizations[4]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_5.image = gradient_image
    button_5.hover_image = hover_gradient_image

    def editempmm():
        main_menu_window.destroy()
        editemployee(curuser, curid)

    button_6 = tk.Button(
        frame,
        text=customizations[5]["text"],
        command=editempmm,
        font=("Arial", 16),
        fg=customizations[4]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_6.image = gradient_image
    button_6.hover_image = hover_gradient_image

    # Place the buttons in the frame
    button_1.place(x=50, y=170, width=300, height=75)
    button_2.place(x=50, y=290, width=300, height=75)
    button_3.place(x=550, y=170, width=300, height=75)
    button_4.place(x=550, y=290, width=300, height=75)
    button_5.place(x=50, y=410, width=300, height=75)
    button_6.place(x=550, y=410, width=300, height=75)

    # Bind mouse events to the buttons for hover effects
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    for button in [
        button_1, button_2, button_3, button_4, button_5
    ]:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    # Create the Cancel button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        main_menu_window,
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

    cancel_button.place(x=675, y=750, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the buttons for hover effect
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    main_menu_window.mainloop()

def chairmanmm(curid="chrmn"):
    curuser = "Chairman"
    # Function to handle button clicks
    def button_click(button_name):
        # Replace this with the actions you want to perform when each button is clicked
        messagebox.showinfo("Button Clicked", f"You clicked the {button_name} button.")

    def cancel_remove_manager():
        main_menu_window.destroy()
        Login()

    main_menu_window = tk.Tk()
    main_menu_window.title("Employee Management System - Main Menu")

    # Make the window full screen
    main_menu_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open(
        "res/mainmenubg.png")  # Replace with your image path
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(main_menu_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame = tk.Frame(main_menu_window, bd=5, relief=tk.SUNKEN)
    frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.6, anchor="center")

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/mainmenuol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Load the gradient image and the hover gradient image
    gradient_image = Image.open(
        "res/#AA0000.png")  # Replace with your gradient image path
    gradient_image = ImageTk.PhotoImage(gradient_image)

    hover_gradient_image = Image.open(
        "res/#CC0000.png")  # Replace with your hover gradient image path
    hover_gradient_image = ImageTk.PhotoImage(hover_gradient_image)

    # Customizations for each button
    customizations = [
        {"text": "Add Employee", "fg": "black"},
        {"text": "Remove Employee", "fg": "black"},
        {"text": "Add Manager", "fg": "black"},
        {"text": "Remove Manager", "fg": "black"},
        {"text": "View Employee", "fg": "black"},
        {"text": "Edit Employee", "fg": "black"}
    ]

    def addempmm():
        main_menu_window.destroy()
        addemployee(curuser)

    button_1 = tk.Button(
        frame,
        text=customizations[0]["text"],
        command=addempmm,
        font=("Arial", 16),
        fg=customizations[0]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_1.image = gradient_image
    button_1.hover_image = hover_gradient_image

    def remempmm():
        main_menu_window.destroy()
        removeemployee(curuser)

    button_2 = tk.Button(
        frame,
        text=customizations[1]["text"],
        command=remempmm,
        font=("Arial", 16),
        fg=customizations[1]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_2.image = gradient_image
    button_2.hover_image = hover_gradient_image

    def addmanagermm():
        main_menu_window.destroy()
        addmanager(curuser)

    button_3 = tk.Button(
        frame,
        text=customizations[2]["text"],
        command=addmanagermm,
        font=("Arial", 16),
        fg=customizations[2]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Continue creating buttons for each option
    button_3.image = gradient_image
    button_3.hover_image = hover_gradient_image

    def remmgrmm():
        main_menu_window.destroy()
        removemanager(curuser)

    button_4 = tk.Button(
        frame,
        text=customizations[3]["text"],
        command=remmgrmm,
        font=("Arial", 16),
        fg=customizations[3]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_4.image = gradient_image
    button_4.hover_image = hover_gradient_image

    def viewempmm():
        main_menu_window.destroy()
        viewemployee(curuser)


    button_5 = tk.Button(
        frame,
        text=customizations[4]["text"],
        command=viewempmm,
        font=("Arial", 16),
        fg=customizations[4]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    button_5.image = gradient_image
    button_5.hover_image = hover_gradient_image

    def editempmm():
        main_menu_window.destroy()
        editemployee(curuser, curid)

    button_6 = tk.Button(
        frame,
        text=customizations[5]["text"],
        command=editempmm,
        font=("Arial", 16),
        fg=customizations[4]["fg"],
        image=gradient_image,
        compound=tk.CENTER,
        borderwidth=0,
    )

    # Store references to the images to prevent garbage collection
    button_6.image = gradient_image
    button_6.hover_image = hover_gradient_image

    # Place the buttons in the frame
    button_1.place(x=50, y=170, width=300, height=75)
    button_2.place(x=50, y=290, width=300, height=75)
    button_3.place(x=550, y=170, width=300, height=75)
    button_4.place(x=550, y=290, width=300, height=75)
    button_5.place(x=50, y=410, width=300, height=75)
    button_6.place(x=550, y=410, width=300, height=75)

    # Bind mouse events to the buttons for hover effects
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    for button in [
        button_1, button_2, button_3, button_4, button_5
    ]:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    # Create the Cancel button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        main_menu_window,
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

    cancel_button.place(x=675, y=750, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the buttons for hover effect
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)
    main_menu_window.mainloop()


def addemployee(curuser):
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
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

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


def addmanager(curuser):
    # Function to handle button clicks
    def add_manager():
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
        name = name_entry.get()
        position = position_entry.get()
        salary = salary_entry.get()
        mobno = mobno_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        # Insert Manager data into the MySQL database
        insert_query = "INSERT INTO manager (ManagerID, Name, Position, Salary, MobNo, Email, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (manager_id, name, position, salary, mobno, email, password)

        try:
            cursor.execute(insert_query, data)
            db.commit()
            messagebox.showinfo("Success", "Manager added successfully!")
        except mysql.connector.Error as err:
            db.rollback()
            messagebox.showerror("Error", f"Failed to add manager: {err}")

        db.close()

    def cancel_add_manager():
        add_manager_window.destroy()
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

    add_manager_window = tk.Tk()
    add_manager_window.title("Manager Management System - Add Manager")

    # Make the window full screen
    add_manager_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/addempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(add_manager_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame = tk.Frame(add_manager_window, bd=5, relief=tk.SUNKEN)
    frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.6, anchor="center")

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/addempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for manager information
    manager_id_label = tk.Label(frame, text=" Manager ID :", font=("Arial", 16))
    manager_id_label.place(x=150, y=75)
    manager_id_entry = tk.Entry(frame, font=("Arial", 14))
    manager_id_entry.place(x=300, y=75, relwidth=0.4)

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

    # Create the Add Manager button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=add_manager,
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
        command=cancel_add_manager,
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

    add_manager_window.mainloop()


def demoteemployee(curuser):
    # Function to handle button clicks
    def demote_employee():
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

        # Check if the new salary is less than the current salary
        get_current_salary_query = "SELECT Salary FROM employee WHERE EmployeeID = %s"
        cursor.execute(get_current_salary_query, (employee_id,))
        current_salary = cursor.fetchone()

        if current_salary and new_salary < current_salary[0]:
            # Update employee's position and salary in the MySQL database
            update_query = "UPDATE employee SET Position = %s, Salary = %s WHERE EmployeeID = %s"
            data = (new_position, new_salary, employee_id)

            try:
                cursor.execute(update_query, data)
                db.commit()
                messagebox.showinfo("Success", "Employee demoted successfully!")
            except mysql.connector.Error as err:
                db.rollback()
                messagebox.showerror("Error", f"Failed to demote employee: {err}")
        else:
            messagebox.showerror("Error", "New salary must be less than the current salary.")

        db.close()

    def cancel_demote_employee():
        demote_employee_window.destroy()
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

    demote_employee_window = tk.Tk()
    demote_employee_window.title("Employee Management System - Demote Employee")

    # Make the window full screen
    demote_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/demempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(demote_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/demempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 750
    frame_height = 500
    center_x = (demote_employee_window.winfo_screenwidth() - frame_width) // 2
    center_y = (demote_employee_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(demote_employee_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/demempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for employee information
    employee_id_label = tk.Label(frame, text="Employee ID:", font=("Arial", 16))
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

    # Create the Demote Employee button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=demote_employee,
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
        command=cancel_demote_employee,
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

    demote_employee_window.mainloop()


def editemployee(curuser, curid):
    # Function to fetch employee details from the database
    def fetch_employee_details(curid):
        # Replace with your MySQL credentials
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="EmployeeDB"
        )

        cursor = db.cursor()
        query = "SELECT * FROM manager WHERE ManagerID = %s"
        cursor.execute(query, (curid,))
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
        update_query = "UPDATE manager SET Name = %s, Email = %s, MobNo = %s WHERE ManagerID = %s"
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

    def cancel_edit_employee():
        edit_employee_window.destroy()
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()


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


    employee_data = fetch_employee_details(curid)

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
        command=cancel_edit_employee,
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


def promoteemployee(curuser):
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
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

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


def removeemployee(curuser):
    # Function to handle button clicks
    def remove_employee():
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
        mobno = mobno_entry.get()

        # Check if the employee exists
        check_query = "SELECT * FROM employee WHERE EmployeeID = %s AND MobNo = %s"
        data = (employee_id, mobno)

        cursor.execute(check_query, data)
        employee = cursor.fetchone()

        if employee:
            # Employee exists, proceed with removal
            remove_query = "DELETE FROM employee WHERE EmployeeID = %s AND MobNo = %s"
            cursor.execute(remove_query, data)
            db.commit()
            messagebox.showinfo("Success", "Employee removed successfully!")
        else:
            # Employee does not exist
            messagebox.showerror("Error", "Employee not found. Please check the Employee ID and Mobile No.")

        db.close()

    def cancel_remove_employee():
        remove_employee_window.destroy()
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

    remove_employee_window = tk.Tk()
    remove_employee_window.title("Employee Management System - Remove Employee")

    # Make the window full screen
    remove_employee_window.attributes("-fullscreen", True)

    # Load and display your background image (update the path to your image)
    bg_image = Image.open("res/remempbg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label with the background image
    bg_label = tk.Label(remove_employee_window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame for better alignment of elements with a curved border
    frame_image = Image.open("res/remempbg.png")
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Calculate the center position for the frame
    frame_width = 750
    frame_height = 500
    center_x = (remove_employee_window.winfo_screenwidth() - frame_width) // 2
    center_y = (remove_employee_window.winfo_screenheight() - frame_height) // 2

    frame = tk.Label(remove_employee_window, image=frame_photo)
    frame.place(x=center_x, y=center_y, width=frame_width, height=frame_height)

    # Create a translucent overlay using a PNG image
    overlay_image = Image.open("res/remempol.png")
    overlay_photo = ImageTk.PhotoImage(overlay_image)

    overlay_label = tk.Label(frame, image=overlay_photo)
    overlay_label.place(relwidth=1, relheight=1)

    # Create labels and entry fields for employee information
    employee_id_label = tk.Label(frame, text="Employee ID:", font=("Arial", 16))
    employee_id_label.place(x=150, y=200)
    employee_id_entry = tk.Entry(frame, font=("Arial", 14))
    employee_id_entry.place(x=300, y=200, relwidth=0.4)

    mobno_label = tk.Label(frame, text="  Mobile No  :", font=("Arial", 16))
    mobno_label.place(x=150, y=275)
    mobno_entry = tk.Entry(frame, font=("Arial", 14))
    mobno_entry.place(x=300, y=275, relwidth=0.4)

    # Create the Remove Employee button
    submit_button_bg = Image.open("res/#0000FF.png")
    submit_button_bg_photo = ImageTk.PhotoImage(submit_button_bg)
    submit_button_hover_bg = Image.open("res/#007FFF.png")
    submit_button_hover_bg_photo = ImageTk.PhotoImage(submit_button_hover_bg)

    submit_button = tk.Button(
        frame,
        text="Submit",
        command=remove_employee,
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
        command=cancel_remove_employee,
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

    remove_employee_window.mainloop()


def removemanager(curuser):
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
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

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


def viewemployee(curuser):
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

    def cancel_remove_manager():
        view_employee_window.destroy()
        if (curuser == "Manager"):
            managermm()
        if (curuser == "Chairman"):
            chairmanmm()

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

    # Create the Cancel button
    cancel_button_bg = Image.open("res/#AA0000.png")
    cancel_button_bg_photo = ImageTk.PhotoImage(cancel_button_bg)
    cancel_button_hover_bg = Image.open("res/#F40009.png")
    cancel_button_hover_bg_photo = ImageTk.PhotoImage(cancel_button_hover_bg)

    cancel_button = tk.Button(
        view_employee_window,
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

    cancel_button.place(x=675, y=750, width=150, height=50)

    # Function to handle hover effect
    def on_enter(event):
        button = event.widget
        button.config(image=button.hover_image)

    def on_leave(event):
        button = event.widget
        button.config(image=button.image)

    # Bind mouse events to the buttons for hover effect
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    # Start the GUI main loop
    view_employee_window.mainloop()






if __name__ == '__main__':
    Login()


