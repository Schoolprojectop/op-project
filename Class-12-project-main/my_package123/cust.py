import customtkinter as a


def customer(a, b, c, d):
    from PIL import Image, ImageTk
    c.geometry("1100x600")
    c.configure(bg='white')

    # Configure grid layout for the window
    c.grid_columnconfigure(0, weight=0)
    c.grid_columnconfigure(1, weight=1)
    c.grid_rowconfigure(0, weight=1)
    c.grid_rowconfigure(1, weight=1)

                      # Load the background image
    bg_image = Image.open("assets/14337.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)
# Create a Label to hold the background image
    bg_label = a.CTkLabel(c, image=bg_photo)      
    bg_label.place(relwidth=1, relheight=1)
                      
    # Left Sidebar Frame
    sidebar_frame = a.CTkFrame(c,
                               width=30,
                               height=500,
                               corner_radius=20,
                               fg_color="whitesmoke",
                               border_color = "black",
                               border_width = 1)
    sidebar_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
    sidebar_frame.grid_rowconfigure((0, 5), weight=1)  # Add empty rows for centering
    sidebar_frame.grid_rowconfigure((1, 2, 3, 4), weight=0)  # Rows for buttons

    #dash
    img1 = ImageTk.PhotoImage(
        Image.open('assets/home.png').resize((30, 30)))
    button1 = a.CTkButton(sidebar_frame,
                          image=img1,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="whitesmoke",
                          hover_color="blue",
                          command=lambda: d("Dash")
                          )
    button1.grid(row=1, column=0, padx=2, pady=10)
    #flight
    img2 = ImageTk.PhotoImage(
        Image.open('assets/plane.png').resize((30, 30)))
    button2 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="whitesmoke",
                          image=img2,
                          hover_color="blue",
                          command=lambda: d("Flight"))
    button2.grid(row=3, column=0, padx=2, pady=10)
    #cust
    img3 = ImageTk.PhotoImage(
        Image.open('assets/cust.png').resize((30, 30)))
    button3 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="blue",
                          image=img3,
                          hover="DISABLE",
                          command=lambda: d("Cust"))
    button3.grid(row=4, column=0, padx=2, pady=10)
    
    img4 = ImageTk.PhotoImage(
        Image.open('assets/map.png').resize((30, 30)))
    button4 = a.CTkButton(sidebar_frame,
                          text="",
                          width=10,
                          height=10,
                          corner_radius=100,
                          fg_color="whitesmoke",
                          image=img4,
                          hover_color="blue",
                          command=lambda: d("Map"))
    button4.grid(row=2, column=0, padx=2, pady=10)

    # Main Frame
    main_frame = a.CTkFrame(c,
                            width=600,
                            height=500,
                            corner_radius=20,
                            fg_color="red")
    main_frame.grid(row=0,
                    column=1,
                    rowspan=2,
                    sticky="nsew",
                    padx=10,
                    pady=10)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)

    # Text Box inside Main Frame
    text_box = a.CTkFrame(main_frame,
                          width=580,
                          height=480,
                          corner_radius=20,
                          fg_color="yellow")
    text_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


# Example usage:
# c = a.CTk()
# create_layout(c)
# c.mainloop()
