# ==========================================================
# Election Software - Main Application
# ----------------------------------------------------------
# Responsibilities:
# - Creates the main Tkinter window
# - Manages all application pages (frames)
# - Displays election data
# - Records the user's vote selections
# - Sends completed votes to the server
#
# This file DOES NOT:
# - Read CSV files
# - Manage candidate images
# - Handle socket connections
# ==========================================================

import tkinter as tk


class ElectionSoftware(tk.Tk):
    def __init__(self):
        super().__init__()

       # Window Settings
        self.title("Election Software")
        self.state("zoomed")          # Fullscreen (Windows)
        self.resizable(True, True)

        self.pages = {}
        self.selected_votes = {}

        self.elections = []

        self.create_pages()

        # Show the first page
        self.show_page("LoginPage")

    def create_pages(self):
        pass

    def show_page(self, page_name):
        page = self.pages.get(page_name)

        if page:
            page.tkraise()


if __name__ == "__main__":
    app = ElectionSoftware()
    app.mainloop()