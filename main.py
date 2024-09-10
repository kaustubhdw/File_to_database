import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import tkinter as tk
from tkinter import filedialog

# MySQL Server Configuration
DB_USERNAME = 'root'   # Replace with your MySQL username
DB_PASSWORD = 'Kaustubh@1234'   # Replace with your MySQL password
DB_HOST = 'localhost'           # Replace with your MySQL host, usually localhost
DB_PORT = 3306                  # Ensure this is an integer
DB_NAME = 'New'  # Replace with your desired database name


def create_database_if_not_exists():
    """Creates the MySQL database if it does not exist."""
    try:
        # Connect to MySQL server without specifying the database
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()
        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created or already exists.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def select_file():
    """Opens a file dialog to select a CSV file."""
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    return file_path

def upload_csv_to_db(file_path):
    """Reads a CSV file and uploads its content to a MySQL database."""
    # Check if the file is a CSV
    if not file_path.endswith('.csv'):
        print("Only CSV files are allowed.")
        return

    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Configure the MySQL database connection using SQLAlchemy
        engine = create_engine(
            f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{int(DB_PORT)}/{DB_NAME}'
        )
        
        # Create a table name based on the CSV file name (without extension)
        table_name = file_path.split("/")[-1].rsplit('.', 1)[0]  # Adjust based on OS path format
        
        # Upload the DataFrame to the MySQL database
        df.to_sql(table_name, engine, index=False, if_exists='replace')
        
        print(f"File '{file_path}' uploaded and saved to the database as table '{table_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create the database if it doesn't exist
    create_database_if_not_exists()
    
    print("Please select a CSV file to upload:")
    file_path = select_file()
    if file_path:
        upload_csv_to_db(file_path)

if __name__ == '__main__':
    main()
