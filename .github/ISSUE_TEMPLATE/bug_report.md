---
name: Bug report
about: Create a report to help us improve
title: ''
labels: good first issue
assignees: ''

---

Description -
The script encounters an error while trying to connect to the MySQL server using SQLAlchemy and mysql-connector-python. The error message indicates that the connection string format is incorrect.

To Reproduce
Steps to reproduce the behavior:

Run the provided Python script that uses SQLAlchemy to connect to a MySQL database.
The script attempts to configure the SQLAlchemy engine with the following connection string:

engine = create_engine(
    f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
The script raises an error during the engine configuration.
Expected behavior
The script should successfully connect to the MySQL server and proceed to read a CSV file and upload its content to the database.

Screenshots
Not applicable.

Desktop (please complete the following information):

OS: [Windows 10] (or specify your OS)
Browser: [Not applicable]
Version: [Not applicable]
Smartphone (please complete the following information):

Device: [Not applicable]
OS: [Not applicable]
Browser: [Not applicable]
Version: [Not applicable]
Additional context

The error message is:
(mysql.connector.errors.InterfaceError) 2003: Can't connect to MySQL server on '%-.100s:%u' (%s) (Warning: %u format: a real number is required, not str)
This indicates that there is a problem with the format of the connection string or parameters used to connect to the MySQL server. Ensure that the placeholders ({DB_USERNAME}, {DB_PASSWORD}, {DB_HOST}, {DB_PORT}, {DB_NAME}) in the connection string are correctly replaced with valid values.

Suggested Fixes:

Verify that the MySQL server is running and accessible.
Check that the connection string format is correct and that all placeholder values are valid.
Confirm that the MySQL port (3306) and host (localhost) are correct and match your server configuration.
