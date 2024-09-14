import pandas as pd
import mysql.connector
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from file_utils import upload_file, file_exists
from db_utils import create_database_if_not_exists, create_table_if_not_exists, insert_data

# Function to create the database from CSV
def create_database_from_csv(host, user, password, db_name, table_name, csv_file):
    if not file_exists(csv_file):
        messagebox.showerror("Error", "The selected file does not exist.")
        return

    try:
        df = pd.read_csv(csv_file)

        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        create_database_if_not_exists(cursor, db_name)
        cursor.execute(f"USE `{db_name}`")
        create_table_if_not_exists(cursor, table_name, df)
        insert_data(cursor, table_name, df)

        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

# Function to launch the file dialog
def choose_file():
    file_path.set(upload_file())

# Function to handle button click and pass inputs to `create_database_from_csv`
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

# Main Tkinter interface
root = Tk()
root.title("Database Creator")

host_var = StringVar()
user_var = StringVar()
password_var = StringVar()
db_name_var = StringVar()
table_name_var = StringVar()
file_path = StringVar()

Label(root, text="MySQL Host").grid(row=0, column=0)
Entry(root, textvariable=host_var).grid(row=0, column=1)

Label(root, text="MySQL User").grid(row=1, column=0)
Entry(root, textvariable=user_var).grid(row=1, column=1)

Label(root, text="MySQL Password").grid(row=2, column=0)
Entry(root, textvariable=password_var, show="*").grid(row=2, column=1)

Label(root, text="Database Name").grid(row=3, column=0)
Entry(root, textvariable=db_name_var).grid(row=3, column=1)

Label(root, text="Table Name").grid(row=4, column=0)
Entry(root, textvariable=table_name_var).grid(row=4, column=1)

Label(root, text="CSV File").grid(row=5, column=0)
Entry(root, textvariable=file_path).grid(row=5, column=1)
Button(root, text="Choose File", command=choose_file).grid(row=5, column=2)

Button(root, text="Submit", command=on_submit).grid(row=6, column=1)

root.mainloop()
