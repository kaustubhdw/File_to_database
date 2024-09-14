import tkinter as tk
from tkinter import messagebox
from file_utils import upload_file
from main import create_database_from_csv  # Ensure this import works without circular issues

def choose_file():
    file_path.set(upload_file())

def on_submit():
    host = host_var.get()
    user = user_var.get()
    password = password_var.get()
    db_name = db_name_var.get()
    table_name = table_name_var.get()
    csv_file = file_path.get()

    if host and user and password and db_name and table_name and csv_file:
        create_database_from_csv(host, user, password, db_name, table_name, csv_file)
    else:
        messagebox.showerror("Error", "Please fill in all the fields and select a CSV file.")

def create_gui():
    global host_var, user_var, password_var, db_name_var, table_name_var, file_path
    
    root = tk.Tk()
    root.title("Database Creator")

    host_var = tk.StringVar()
    user_var = tk.StringVar()
    password_var = tk.StringVar()
    db_name_var = tk.StringVar()
    table_name_var = tk.StringVar()
    file_path = tk.StringVar()

    tk.Label(root, text="MySQL Host").grid(row=0, column=0)
    tk.Entry(root, textvariable=host_var).grid(row=0, column=1)

    tk.Label(root, text="MySQL User").grid(row=1, column=0)
    tk.Entry(root, textvariable=user_var).grid(row=1, column=1)

    tk.Label(root, text="MySQL Password").grid(row=2, column=0)
    tk.Entry(root, textvariable=password_var, show="*").grid(row=2, column=1)

    tk.Label(root, text="Database Name").grid(row=3, column=0)
    tk.Entry(root, textvariable=db_name_var).grid(row=3, column=1)

    tk.Label(root, text="Table Name").grid(row=4, column=0)
    tk.Entry(root, textvariable=table_name_var).grid(row=4, column=1)

    tk.Label(root, text="CSV File").grid(row=5, column=0)
    tk.Entry(root, textvariable=file_path).grid(row=5, column=1)
    tk.Button(root, text="Choose File", command=choose_file).grid(row=5, column=2)

    tk.Button(root, text="Submit", command=on_submit).grid(row=6, column=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
