import pyodbc
from dotenv import load_dotenv
import os

# Load env variables from .env file
load_dotenv()

def create_connection():
    # remem: defined in .env file !!!
    server = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')

    try:
        conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};\
            DATABASE={database}; UID={username};Trusted_Connection=yes;'
        )

        # print("Connection established") for tests
        return conn
    
    except pyodbc.Error as e:
        # print("Error", e) for tests x2
        return None
    
# create_connection() uncommented for testing purposes :D
