from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

def upload_file():
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filename:
        print(f"Selected file: {filename}")
    else:
        print("No file selected!")
    return filename

def file_exists(file_path):
    return os.path.exists(file_path)
