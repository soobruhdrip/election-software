import tkinter as tk
from tkinter import messagebox
import socket
from PIL import Image, ImageTk
import os

def on_close():
    messagebox.showinfo("Notice", "Chup Chap Vote Kar")

def disable_alt_f4(event):
    messagebox.showinfo("Notice", "Chup Chap Vote Kar")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DAV ELECTIONS")
        self.attributes("-fullscreen", True)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", on_close)
        self.bind_all("<Alt-F4>", disable_alt_f4)
        self.frames = {}
        for F in (LoginPage, Page1, Page2, Page3, Page4, Page5, Page6):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        if page_class == Page6:
            frame.update_review() 
        frame.tkraise()

        
#--------------------------------------------FRAME0--------------------------------------------

class LoginPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        try:
            self.bg_image = tk.PhotoImage(file=r"D:\Elections\11th\png\background\lgn.png")    #File Location For Background
            bg_label = tk.Label(self, image=self.bg_image)
            bg_label.place(relwidth=1, relheight=1)
        except tk.TclError:
            print("Error loading background image.")

        login_frame = tk.LabelFrame(self, bd=2, relief="solid", padx=15, pady=15)
        login_frame.place(relx=0.86, rely=0.65, anchor="center")

        label_pass = tk.Label(login_frame, text="Password:", font=("Verdana", 12))
        label_pass.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        
        self.entry_pass = tk.Entry(login_frame, show="◾", font=("Verdana", 12), width=15)
        self.entry_pass.grid(row=0, column=1, padx=5, pady=5)

        login_button = tk.Button(login_frame, text="Login", font=("Verdana", 13), width=10, pady=5, command=self.check_login)
        login_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    def reset(self):
        self.entry_pass.delete(0, tk.END)

    def check_login(self):
        password = self.entry_pass.get()
        if password == "!&": #Password
            self.master.show_frame(Page1)
        else:
            messagebox.showerror("Login Failed", "Invalid password. Please try again.")
            self.entry_pass.delete(0, tk.END)
            
#--------------------------------------------FRAME1--------------------------------------------
# WELCOMEPAGE
            
class Page1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

       
        img1 = tk.PhotoImage(file=r"D:\Elections\11th\png\background\wlc.png")  #File Location For Background
        lbl = tk.Label(self, image=img1)
        lbl.image = img1
        lbl.place(relwidth=1, relheight=1) 

        #Next Button
        next_button = tk.Button(
            self,
            text="Next",
            font=("Verdana", 18, "bold"),bg='#365942',fg='white',
            padx=20, pady=10,
            command=lambda: parent.show_frame(Page2)
        )
        next_button.place(relx=0.5, rely=0.9, anchor="center")
        
#--------------------------------------------FRAME2--------------------------------------------
# CAPTAIN BOYS

class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title = "CAPTAIN BOYS"

        try:
            img2 = tk.PhotoImage(file=r"D:\Elections\11th\png\background\cb.png")   #File Location For Background
            lbl2 = tk.Label(self, image=img2)
            lbl2.image = img2
            lbl2.grid(row=0, column=0, sticky="nsew")
        except tk.TclError:
            print("Error loading background image.")

        self.radio_var = tk.StringVar(value="")

        options_frame = tk.Frame(self)
        options_frame.place(relx=0.5, rely=0.5, anchor="center")

        option_img_paths = [
            r"D:\Elections\11th\png\Candidates\cb1.png",
            r"D:\Elections\11th\png\Candidates\cb2.png",
            r"D:\Elections\11th\png\Candidates\cb3.png",
            r"D:\Elections\11th\png\Candidates\cb4.png",        #File Location For Candidate's Images
        ]

        option_names = ["Praneel Deshmukh", "Abhichandra Charke", "Aadityaraje Desai", "Rachit Srivastav"]      #Candidate Names

        self.option_images = []
        self.option_radiobuttons = []
        self.option_image_buttons = []

        def on_option_selected(value):
            self.radio_var.set(value)
            self.update_selection_borders()

        for i, path in enumerate(option_img_paths):
            try:
                img = Image.open(path)
                img_small = img.resize((230, 230), Image.LANCZOS) #Resize here
                img_small = ImageTk.PhotoImage(img_small)
                self.option_images.append(img_small)

                option_container = tk.Frame(options_frame, padx=0, pady=0) 
                option_container.grid(row=0, column=i, padx=8, pady=6)

                btn = tk.Button(option_container, image=img_small, bd=2, relief='solid',
                                highlightthickness=0, highlightbackground='#555555',
                                command=lambda v=f"Option{i+1}": on_option_selected(v),
                                padx=0, pady=0) 
                btn.pack()

                label = tk.Label(option_container, text=option_names[i], font=("Verdana", 12))
                label.pack(pady=(6, 6))

                rbtn = tk.Radiobutton(option_container, variable=self.radio_var, value=f"Option{i+1}",
                                      command=lambda v=f"Option{i+1}": on_option_selected(v), indicatoron=1)
                rbtn.pack(pady=(0, 0))
                self.option_radiobuttons.append(rbtn)

                btn.bind("<Button-1>", lambda e, rb=rbtn: rb.select())
                self.option_image_buttons.append(btn)

            except Exception as e:
                print(f"Error loading image: {path}, {e}")

        def update_selection_borders():
            selected = self.radio_var.get()
            for idx, btn in enumerate(self.option_image_buttons):
                if f"Option{idx+1}" == selected:
                    btn.config(highlightthickness=4, highlightbackground="green", bd=5, relief='solid')
                else:
                    btn.config(highlightthickness=0, highlightbackground='#555555', bd=0, relief='solid')

        self.update_selection_borders = update_selection_borders
        self.radio_var.trace_add("write", lambda *args: self.update_selection_borders())

        def on_next_click():
            if self.radio_var.get() == "":
                messagebox.showwarning("Warning", "You have to vote at least ONE before proceeding")
            else:
                self.master.show_frame(Page3)

        #Next Button
        next_button = tk.Button(self, text="Next", font=("Verdana", 18, "bold"),bg='#365942',fg='white',
                                padx=0, pady=0, command=on_next_click) 
        next_button.place(relx=0.5, rely=0.85, anchor="s")

#--------------------------------------------FRAME3--------------------------------------------
# CAPTAIN GIRLS

class Page3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title = "CAPTAIN GIRLS"

        try:
            img3 = tk.PhotoImage(file=r"D:\Elections\11th\png\background\cg.png")   #File Location For Background
            lbl3 = tk.Label(self, image=img3)
            lbl3.image = img3 
            lbl3.grid(row=0, column=0, sticky="nsew")
        except tk.TclError:
            print("Error loading background image.")

        self.radio_var = tk.StringVar(value="")

        options_frame = tk.Frame(self)
        options_frame.place(relx=0.5, rely=0.5, anchor="center")

        option_img_paths = [
            r"D:\Elections\11th\png\Candidates\cg1.png",
            r"D:\Elections\11th\png\Candidates\cg2.png",
            r"D:\Elections\11th\png\Candidates\cg3.png",
            r"D:\Elections\11th\png\Candidates\cg4.png",        #File Location For Candidate's Images
        ]

        option_names = ["Gauravi Zade", "Naisha Rastogi", "Trisha Shah", "Kirthika Jaychander"]         #Candidate Names

        self.option_images = []
        self.option_radiobuttons = []
        self.option_image_buttons = []

        def on_option_selected(value):
            self.radio_var.set(value)
            self.update_selection_borders()

        for i, path in enumerate(option_img_paths):
            try:
                img = Image.open(path)
                img_small = img.resize((225, 225), Image.LANCZOS)  
                img_small = ImageTk.PhotoImage(img_small)
                self.option_images.append(img_small)

                option_container = tk.Frame(options_frame, padx=0, pady=0) 
                option_container.grid(row=0, column=i, padx=8, pady=6)

                btn = tk.Button(option_container, image=img_small, bd=2, relief='solid',
                                highlightthickness=0, highlightbackground='#555555',
                                command=lambda v=f"Option{i+1}": on_option_selected(v),
                                padx=0, pady=0)  
                btn.pack()

                label = tk.Label(option_container, text=option_names[i], font=("Verdana", 12))
                label.pack(pady=(6, 6))

                rbtn = tk.Radiobutton(option_container, variable=self.radio_var, value=f"Option{i+1}",
                                      command=lambda v=f"Option{i+1}": on_option_selected(v), indicatoron=1)
                rbtn.pack(pady=(0, 0))
                self.option_radiobuttons.append(rbtn)

                btn.bind("<Button-1>", lambda e, rb=rbtn: rb.select())
                self.option_image_buttons.append(btn)

            except Exception as e:
                print(f"Error loading image: {path}, {e}")

        def update_selection_borders():
            selected = self.radio_var.get()
            for idx, btn in enumerate(self.option_image_buttons):
                if f"Option{idx+1}" == selected:
                    btn.config(highlightthickness=4, highlightbackground="blue", bd=5, relief='solid')
                else:
                    btn.config(highlightthickness=0, highlightbackground='#555555', bd=0, relief='solid')

        self.update_selection_borders = update_selection_borders
        self.radio_var.trace_add("write", lambda *args: self.update_selection_borders())

        def on_next_click():
            if self.radio_var.get() == "":
                messagebox.showwarning("Warning", "You have to vote at least ONE before proceeding")
            else:
                self.master.show_frame(Page4)

        next_button = tk.Button(self, text="Next", font=("Verdana", 18, "bold"),bg='#365942',fg='white',
                                padx=0, pady=0, command=on_next_click) 
        next_button.place(relx=0.5, rely=0.85, anchor="s")

#--------------------------------------------FRAME4--------------------------------------------
# VICE CAPTAIN BOYS

class Page4(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title = "VICE CAPTAIN BOYS"

        try:
            img4 = tk.PhotoImage(file=r"D:\Elections\11th\png\background\vcb.png")   #File Location For Background
            lbl4 = tk.Label(self, image=img4)
            lbl4.image = img4  
            lbl4.grid(row=0, column=0, sticky="nsew")
        except tk.TclError:
            print("Error loading background image.")

        self.radio_var = tk.StringVar(value="")

        options_frame = tk.Frame(self)
        options_frame.place(relx=0.5, rely=0.55, anchor="center")

        option_img_paths = [
            r"D:\Elections\11th\png\Candidates\vcb1.png",
            r"D:\Elections\11th\png\Candidates\vcb2.png",
            r"D:\Elections\11th\png\Candidates\vcb3.png",
            r"D:\Elections\11th\png\Candidates\vcb4.png",
            r"D:\Elections\11th\png\Candidates\vcb5.png",  #File Location For Candidate's Images
        ]

        option_names = ["Sagnik Ghosh", "Kausar Chandra", "Avaneesh Mahalle", "Viren Jadhav", "Krishna Yadav"]      #Candidate Names

        self.option_images = []
        self.option_radiobuttons = []
        self.option_image_buttons = []

        def on_option_selected(value):
            self.radio_var.set(value)
            self.update_selection_borders()

        for i, path in enumerate(option_img_paths):
            try:
                img = Image.open(path)
                img_small = img.resize((185, 185), Image.LANCZOS) #Resize 
                img_small = ImageTk.PhotoImage(img_small)
                self.option_images.append(img_small)

                option_container = tk.Frame(options_frame, padx=0, pady=0) 
                option_container.grid(row=0, column=i, padx=8, pady=6) 

                btn = tk.Button(option_container, image=img_small, bd=2, relief='solid',
                                highlightthickness=0, highlightbackground='#555555',
                                command=lambda v=f"Option{i+1}": on_option_selected(v),
                                padx=0, pady=0)  
                btn.pack()

                label = tk.Label(option_container, text=option_names[i], font=("Verdana", 12))
                label.pack(pady=(6, 6))

                rbtn = tk.Radiobutton(option_container, variable=self.radio_var, value=f"Option{i+1}",
                                      command=lambda v=f"Option{i+1}": on_option_selected(v), indicatoron=1)
                rbtn.pack(pady=(0, 0))
                self.option_radiobuttons.append(rbtn)

                btn.bind("<Button-1>", lambda e, rb=rbtn: rb.select())
                self.option_image_buttons.append(btn)

            except Exception as e:
                print(f"Error loading image: {path}, {e}")

        def update_selection_borders():
            selected = self.radio_var.get()
            for idx, btn in enumerate(self.option_image_buttons):
                if f"Option{idx+1}" == selected:
                    btn.config(highlightthickness=4, highlightbackground="blue", bd=5, relief='solid')
                else:
                    btn.config(highlightthickness=0, highlightbackground='#555555', bd=0, relief='solid')

        self.update_selection_borders = update_selection_borders
        self.radio_var.trace_add("write", lambda *args: self.update_selection_borders())

        def on_next_click():
            if self.radio_var.get() == "":
                messagebox.showwarning("Warning", "You have to vote at least ONE before proceeding")
            else:
                self.master.show_frame(Page5)
        #Next Button
        next_button = tk.Button(self, text="Next", font=("Verdana", 18, "bold"),bg='#365942',fg='white',
                                padx=0, pady=0, command=on_next_click) 
        next_button.place(relx=0.5, rely=0.85, anchor="s")

#--------------------------------------------FRAME5--------------------------------------------
# VICE CAPTAIN GIRLS

class Page5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        try:
            img5 = tk.PhotoImage(file=r"D:\Elections\11th\png\background\vcg.png")   #File Location For Background
            lbl5 = tk.Label(self, image=img5)
            lbl5.image = img5  
            lbl5.grid(row=0, column=0, sticky="nsew")
        except tk.TclError:
            print("Error loading background image.")

        self.radio_var = tk.StringVar(value="")

        options_frame = tk.Frame(self)
        options_frame.place(relx=0.5, rely=0.55, anchor="center")


        option_img_paths = [
            r"D:\Elections\11th\png\Candidates\vcg1.png",
            r"D:\Elections\11th\png\Candidates\vcg2.png",
            r"D:\Elections\11th\png\Candidates\vcg3.png",
            r"D:\Elections\11th\png\Candidates\vcg4.png",
            r"D:\Elections\11th\png\Candidates\vcg5.png",       #File Location For Candidate's Images
        ]
        option_names = [
            "Sumedha Vaidya", 
            "Trisha Kandpal", 
            "Ketaki Phalle", 
            "Riya Shirode", 
            "Kavya Mehta"
        ]           #Candidate Names

        self.option_images = []
        self.option_radiobuttons = []
        self.option_image_buttons = []

        def on_option_selected(value):
            self.radio_var.set(value)
            self.update_selection_borders()

        for i, path in enumerate(option_img_paths):
            try:
                img = Image.open(path)
                img_small = img.resize((185, 185), Image.LANCZOS)
                img_small = ImageTk.PhotoImage(img_small)
                self.option_images.append(img_small)

                option_container = tk.Frame(options_frame, padx=0, pady=0)
                option_container.grid(row=0, column=i, padx=8, pady=6)

                btn = tk.Button(
                    option_container, 
                    image=img_small, 
                    bd=2, 
                    relief='solid',
                    highlightthickness=0, 
                    highlightbackground='#555555',
                    command=lambda v=f"Option{i+1}": on_option_selected(v),
                    padx=0, 
                    pady=0
                )
                btn.pack()

                label = tk.Label(
                    option_container, 
                    text=option_names[i], 
                    font=("Verdana", 12)
                )
                label.pack(pady=(6, 6))

                rbtn = tk.Radiobutton(
                    option_container, 
                    variable=self.radio_var, 
                    value=f"Option{i+1}",
                    command=lambda v=f"Option{i+1}": on_option_selected(v), 
                    indicatoron=1
                )
                rbtn.pack(pady=(0, 0))
                self.option_radiobuttons.append(rbtn)

                btn.bind("<Button-1>", lambda e, rb=rbtn: rb.select())
                self.option_image_buttons.append(btn)

            except Exception as e:
                print(f"Error loading image: {path}, {e}")

        def update_selection_borders():
            selected = self.radio_var.get()
            for idx, btn in enumerate(self.option_image_buttons):
                if f"Option{idx+1}" == selected:
                    btn.config(
                        highlightthickness=4, 
                        highlightbackground="blue", 
                        bd=5, 
                        relief='solid'
                    )
                else:
                    btn.config(
                        highlightthickness=0, 
                        highlightbackground='#555555', 
                        bd=0, 
                        relief='solid'
                    )

        self.update_selection_borders = update_selection_borders
        self.radio_var.trace_add("write", lambda *args: self.update_selection_borders())

        #Next Button
        next_button = tk.Button(
            self, 
            text="Next", 
            font=("Verdana", 18, "bold"),bg='#365942',fg='white',
            padx=0, 
            pady=0, 
            command=self.on_next_click
        ) 
        next_button.place(relx=0.5, rely=0.85, anchor="s")

    def on_next_click(self):
        if self.radio_var.get() == "":
            messagebox.showwarning("Warning", "You must select one candidate to proceed")
        else:
            self.master.show_frame(Page6)

#--------------------------------------------FRAME6--------------------------------------------
# REVIEW PAGE

class Page6(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#f0f0f0")
        
        main_frame = tk.Frame(self, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        title_label = tk.Label(main_frame, text="YOUR VOTES", font=("Verdana", 24, "bold"), bg="#f0f0f0", pady=10)
        title_label.pack(fill="x")

        categories_container = tk.Frame(main_frame, bg="#f0f0f0")
        categories_container.pack(fill="both", expand=True)

        positions = [
            ("CAPTAIN BOYS", "#e6f2ff"),
            ("CAPTAIN GIRLS", "#ffe6f2"),
            ("VICE CAPTAIN BOYS", "#e6ffe6"),
            ("VICE CAPTAIN GIRLS", "#fff2e6") #Background Colours & Title
        ]

        self.position_frames = []
        self.image_labels = []
        self.name_labels = []

        for i, (title, color) in enumerate(positions):
            row = i // 2
            col = i % 2
            
            frame = self.create_category_frame(categories_container, title, color)
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            self.position_frames.append(frame)
            
            img_label = tk.Label(frame, bg=color)
            img_label.pack(pady=10)
            self.image_labels.append(img_label)
            
            name_label = tk.Label(frame, font=("Verdana", 14), bg=color)
            name_label.pack()
            self.name_labels.append(name_label)
            
            categories_container.grid_rowconfigure(row, weight=1)
            categories_container.grid_columnconfigure(col, weight=1)


        button_frame = tk.Frame(main_frame, bg="#f0f0f0", pady=10)
        button_frame.pack(fill="x")

        self.confirm_button = tk.Button(
            button_frame,
            text="Confirm Votes",
            font=("Verdana", 18, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=30,
            pady=20,
            command=self.show_submit
        )
        self.confirm_button.pack(side="left", expand=True)

        self.submit_button = tk.Button(
            button_frame,
            text="Submit Votes",
            font=("Verdana", 18, "bold"),
            bg="#f44336", 
            fg="white",
            padx=30,
            pady=20,
            command=self.submit_votes
        )
        self.submit_button.pack(side="left", expand=True)
        self.submit_button.pack_forget()
        
    def create_category_frame(self, parent, title, bg_color):
        """Helper to create styled category frames"""
        frame = tk.Frame(parent, bd=2, relief="groove", padx=15, pady=15, bg=bg_color)
        label = tk.Label(frame, text=title, font=("Verdana", 18, "bold"), bg=bg_color)
        label.pack(anchor="center")
        return frame

    def show_submit(self):
        """Switch from confirm to submit button"""
        self.confirm_button.pack_forget()
        self.submit_button.pack(side="left", expand=True)

    def update_review(self):
        names = {
            "Page2": ["Praneel Deshmukh", "Abhichandra Charke", "Aadityaraje Desai", "Rachit Srivastav"],
            "Page3": ["Gauravi Zade", "Naisha Rastogi", "Trisha Shah", "Kirthika Jaychander"],
            "Page4": ["Sagnik Ghosh", "Kausar Chandra", "Avaneesh Mahalle", "Viren Jadhav", "Krishna Yadav"],
            "Page5": ["Sumedha Vaidya", "Trisha Kandpal", "Ketaki Phalle", "Riya Shirode", "Kavya Mehta"]       #Candidate's Names
        }

        image_paths = {
            "Page2": ["cb1.png", "cb2.png", "cb3.png", "cb4.png"],
            "Page3": ["cg1.png", "cg2.png", "cg3.png", "cg4.png"],
            "Page4": ["vcb1.png", "vcb2.png", "vcb3.png", "vcb4.png", "vcb5.png"],
            "Page5": ["vcg1.png", "vcg2.png", "vcg3.png", "vcg4.png", "vcg5.png"]
        }               #File Location For Candidate's Images

        for i, page in enumerate([Page2, Page3, Page4, Page5]):
            selection = self.master.frames[page].radio_var.get()
            page_name = page.__name__
            
            if selection:
                idx = int(selection.replace("Option", "")) - 1
                self.name_labels[i].config(text=names[page_name][idx])
                
                try:
                    img_path = f"D:\\Elections\\11th\\png\\Candidates\\{image_paths[page_name][idx]}" #Image Path 
                    img = Image.open(img_path)
                    img = img.resize((227, 227), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    self.image_labels[i].config(image=img)
                    self.image_labels[i].image = img  
                except:
                    self.image_labels[i].config(image='', text='Image Not Available')
            else:
                self.name_labels[i].config(text="No selection")
                self.image_labels[i].config(image='', text='No Image')

    def submit_votes(self):
        """Process and send the votes"""
        names = {
            "CAPTAIN BOYS": ["Praneel Deshmukh", "Abhichandra Charke", "Aadityaraje Desai", "Rachit Srivastav"],
            "CAPTAIN GIRLS": ["Gauravi Zade", "Naisha Rastogi", "Trisha Shah", "Kirthika Jaychander"],
            "VICE CAPTAIN BOYS": ["Sagnik Ghosh", "Kausar Chandra", "Avaneesh Mahalle", "Viren Jadhav", "Krishna Yadav"],
            "VICE CAPTAIN GIRLS": ["Sumedha Vaidya", "Trisha Kandpal", "Ketaki Phalle", "Riya Shirode", "Kavya Mehta"] #Candidate Names
        }

        vote_data = []
        for position, page in [
            ("CAPTAIN BOYS", Page2),
            ("CAPTAIN GIRLS", Page3),
            ("VICE CAPTAIN BOYS", Page4),
            ("VICE CAPTAIN GIRLS", Page5) 
        ]:
            selection = self.master.frames[page].radio_var.get()
            if selection:
                idx = int(selection.replace("Option", "")) - 1
                vote_data.append(names[position][idx])
            else:
                vote_data.append("Not Selected")

        self.send_votes_to_server(*vote_data)

        messagebox.showinfo("Success", "Votes submitted successfully!")
        
        for page in [Page2, Page3, Page4, Page5]:
            self.master.frames[page].radio_var.set("")
        
        self.submit_button.pack_forget()
        self.confirm_button.pack(side="left", expand=True)
        self.master.frames[LoginPage].reset()
        self.master.show_frame(LoginPage)

    def send_votes_to_server(self, captain_boys, captain_girls, vice_captain_boys, vice_captain_girls):
        """Network handler for vote submission"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('IPADDRESS', 65432)) #Add IP Address here
                data = f"{captain_boys},{captain_girls},{vice_captain_boys},{vice_captain_girls}"
                s.sendall(data.encode('utf-8'))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send votes: {str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
