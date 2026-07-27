# ==========================================================
# Election Software - Login Page
# ----------------------------------------------------------
# Responsibilities:
# - Displays the login screen
# - Verifies the login password
# - Navigates to the Welcome page on success
# - Allows the user to exit the application
#
# This page DOES NOT:
# - Read CSV files
# - Handle networking
# - Load candidate information
# ==========================================================

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import assets
import config


class LoginPage(tk.Frame):
    """
    Login page for the Election Software.
    """

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Load Background Image
        # --------------------------------------------------
        try:
            image = Image.open(assets.LOGIN_BG)

            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            image = image.resize(
                (screen_width, screen_height),
                Image.LANCZOS
            )

            self.background_image = ImageTk.PhotoImage(image)

            background_label = tk.Label(
                self,
                image=self.background_image
            )

            background_label.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1
            )

        except Exception as error:
            print(f"Error loading background image:\n{error}")

        # --------------------------------------------------
        # Login Frame
        # --------------------------------------------------
        login_frame = tk.LabelFrame(
            self,
            bd=2,
            relief="solid",
            padx=15,
            pady=15
        )

        login_frame.place(
            relx=0.86,
            rely=0.65,
            anchor="center"
        )

        # --------------------------------------------------
        # Password Label
        # --------------------------------------------------
        password_label = tk.Label(
            login_frame,
            text="Password:",
            font=("Verdana", 12)
        )

        password_label.grid(
            row=0,
            column=0,
            sticky="e",
            padx=5,
            pady=5
        )

        # --------------------------------------------------
        # Password Entry
        # --------------------------------------------------
        self.password_entry = tk.Entry(
            login_frame,
            show="◾",
            font=("Verdana", 12),
            width=15
        )

        self.password_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # --------------------------------------------------
        # Login Button
        # --------------------------------------------------
        login_button = tk.Button(
            login_frame,
            text="Login",
            font=("Verdana", 13),
            width=10,
            pady=5,
            command=self.check_login
        )

        login_button.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(10, 5)
        )

        # --------------------------------------------------
        # Exit Button
        # --------------------------------------------------
        exit_button = tk.Button(
            login_frame,
            text="Exit",
            font=("Verdana", 13),
            width=10,
            pady=5,
            command=self.exit_program
        )

        exit_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(5, 0)
        )

    # ======================================================
    # Page Functions
    # ======================================================

    def reset(self):
        """
        Clears the password entry box.
        """

        self.password_entry.delete(0, tk.END)

    def check_login(self):
        """
        Verifies the entered password.
        """

        password = self.password_entry.get()

        if password == config.PASSWORD:

            self.reset()

            # Navigate to the Welcome Page
            self.master.show_page("WelcomePage")

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid password. Please try again."
            )

            self.reset()

    def exit_program(self):
        """
        Closes the application after confirmation.
        """

        confirm = messagebox.askyesno(
            "Exit Election Software",
            "Are you sure you want to exit?"
        )

        if confirm:
            self.master.destroy()