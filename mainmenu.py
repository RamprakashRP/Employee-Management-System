import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from AddEmployee import addemployee
from AddManager import addmanager
from DemoteEmployee import demoteemployee
from EditEmployee import editemployee
from PromoteEmployee import promoteemployee
from RemoveEmployee import removeemployee
from RemoveManager import removemanager
from ViewEmployee import viewemloyee


def managermm():
    # Function to handle button clicks
    def button_click(button_name):
        # Replace this with the actions you want to perform when each button is clicked
        messagebox.showinfo("Button Clicked", f"You clicked the {button_name} button.")

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
        addemployee()

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
        removeemployee()

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
        promoteemployee()

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
        demoteemployee()

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
        viewemloyee()

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
        editemployee()

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

    main_menu_window.mainloop()

def chairmanmm():
    # Function to handle button clicks
    def button_click(button_name):
        # Replace this with the actions you want to perform when each button is clicked
        messagebox.showinfo("Button Clicked", f"You clicked the {button_name} button.")

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
        addemployee()

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
        removeemployee()

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
        addmanager()

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
        removemanager()

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
        viewemloyee()


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
        editemployee()

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

    main_menu_window.mainloop()

chairmanmm()