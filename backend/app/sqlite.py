import csv
import sqlite3
from constants import *

def execute_query(query):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()
    cursor.close()
    connection.close()
    return result

def create_table(table_name):
    try:
        # importing csv and extracting the data
        with open(DATA_CSV,'r') as file:
            reader = csv.DictReader(file)
            observations = [(i['DATE'],i['PATIENT'],i['ENCOUNTER'],i['CODE'],i['DESCRIPTION'],
                i['VALUE'],i['UNITS'],i['TYPE']) for i in reader]
            
        # connect to database. Will create test.db if it does not yet exist
        connection = sqlite3.connect(DB_PATH)
        # creates a cursor that allows interaction with the database
        cursor = connection.cursor()

        # creating the table, called test, in the database
        cursor.execute(f"""
            CREATE TABLE {DB_TABLE_NAME} (
                `date` DATE DEFAULT NULL,
                PATIENT text(100) DEFAULT NULL,
                ENCOUNTER text(100) DEFAULT NULL,
                CODE text(100) DEFAULT NULL,
                DESCRIPTION text(255) DEFAULT NULL,
                VALUE text(100) DEFAULT NULL,
                UNITS text(100) DEFAULT NULL,
                `TYPE` text(100) DEFAULT NULL
            )
        """)
        cursor.executemany(f'INSERT INTO {table_name} (DATE,PATIENT,ENCOUNTER,CODE,DESCRIPTION,VALUE,UNITS,TYPE) VALUES (?,?,?,?,?,?,?,?)',observations)
        connection.commit()
        cursor.close()
        connection.close()

    except sqlite3.Error as error:
        print(f"Error: {error}")

def test_db():
    print(execute_query(f'select * from {DB_TABLE_NAME} where PATIENT="10339b10-3cd1-4ac3-ac13-ec26728cb592" limit 1'))

if __name__ == "__main__":
    create_table(DB_TABLE_NAME)
    test_db()