import mysql.connector as conn
from dotenv import load_dotenv
import os

class DB:
    def __init__(self):
        load_dotenv()
        self.con=conn.connect(host=os.getenv('DB_HOST'), database=os.getenv('DB_SCHEMA'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'))
        if self.con.is_connected():
            print("Connection successful")
        else:
            print("Connection failed")
    
    def createTable(self):
        pass

    def insertIntoTable(self):
        pass

    def readFromTable(self):
        pass

    def updateRow(self):
        pass

    def deleteRow(self):
        pass

db = DB()