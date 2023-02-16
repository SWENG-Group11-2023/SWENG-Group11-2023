import csv
import sqlite3
from constants import *

def ExecuteQuery(query:str):
    # connect to database. Will create test.db if it does not yet exist
    connection = sqlite3.connect(DB_PATH)
    # creates a cursor that allows interaction with the database
    cursor = connection.cursor()

    result = cursor.execute(query).fetchall()
    cursor.close()
    connection.close()
    return result

def main():
    # SQL query to select the rows where the patient "10339b10-3cd1-4ac3-ac13-ec26728cb592" is in. Currently limited to 1.
    print(ExecuteQuery('select * from test where PATIENT="10339b10-3cd1-4ac3-ac13-ec26728cb592" limit 1'))

    # SQL query to select the rows where the patient "1d604da9-9a81-4ba9-80c2-de3375d59b40" is in. Currently limited to 1.
    print(ExecuteQuery('select * from test where PATIENT="1d604da9-9a81-4ba9-80c2-de3375d59b40" limit 1'))

    # SQL query to select the rows where the encounter "7ff86631-0378-4bfc-92ce-1edd697eb18e" is in. Currently limited to 1.
    print(ExecuteQuery('select * from test where ENCOUNTER="7ff86631-0378-4bfc-92ce-1edd697eb18e" limit 1'))

if __name__ == "__main__":
    main()