import mysql.connector
import pandas as pd

def infer_mysql_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "TINYINT(1)"
    else:
        return "VARCHAR(255)"

def create_database_if_not_exists(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
    print(f"Database `{db_name}` created or already exists.")

def create_table_if_not_exists(cursor, table_name, df):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()

    if result:
        print(f"Table `{table_name}` already exists.")
    else:
        columns = ', '.join([f"`{col}` {infer_mysql_dtype(df[col].dtype)}" for col in df.columns])
        create_table_query = f"CREATE TABLE `{table_name}` ({columns})"
        cursor.execute(create_table_query)
        print(f"Table `{table_name}` created successfully.")

def insert_data(cursor, table_name, df):
    for _, row in df.iterrows():
        values = ', '.join([f"'{str(val)}'" for val in row])
        insert_query = f"INSERT INTO `{table_name}` VALUES ({values})"
        cursor.execute(insert_query)
    print("Data inserted successfully!")
