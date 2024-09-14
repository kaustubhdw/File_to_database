import pandas as pd
import mysql.connector
from tkinter import messagebox
from db_utils import create_database_if_not_exists, create_table_if_not_exists, insert_data
from file_utils import file_exists

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
