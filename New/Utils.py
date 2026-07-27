# ==========================================================
# Election Software - Utility Functions
# ----------------------------------------------------------
# Responsibilities:
# - Stores reusable helper functions
# - Prevents duplicate code across multiple pages
# - Resize images
# - Load images
# - Clear frames
# - Centre windows
#
# This file DOES NOT:
# - Read CSV files
# - Handle networking
# - Manage election logic
# ==========================================================

from PIL import Image, ImageTk


def load_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()