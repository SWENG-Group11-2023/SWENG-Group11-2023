import csv
import sqlite3
import time

def CreateDatabase():
    try:
        # importing csv and extracting the data
        with open('./data/observations_clean.csv','r') as file:
            reader = csv.DictReader(file)
            observations = [(i['DATE'],i['PATIENT'],i['ENCOUNTER'],i['CODE'],i['DESCRIPTION'],
                i['VALUE'],i['UNITS'],i['TYPE']) for i in reader]
            
        # connect to database. Will create test.db if it does not yet exist
        connection = sqlite3.connect('./test.db')
        # creates a cursor that allows interaction with the database
        cursor = connection.cursor()

        # creating the table, called test, in the database
        cursor.execute("""
        CREATE TABLE test (
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
        cursor.executemany('INSERT INTO test (DATE,PATIENT,ENCOUNTER,CODE,DESCRIPTION,VALUE,UNITS,TYPE) VALUES (?,?,?,?,?,?,?,?)',observations)
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print("error occurred on import")

def ExecuteQuery(query:str):
    # connect to database. Will create test.db if it does not yet exist
    connection = sqlite3.connect('./test.db')
    # creates a cursor that allows interaction with the database
    cursor = connection.cursor()

    result = cursor.execute(query).fetchall()
    cursor.close()
    connection.close()
    return result

def main():
    # comment out next line after running file once. 
    # CreateDatabase()

    # once you have created the database comment out line 50 and uncomment line 56.
   
    # sample SQL query to select the rows where the patient "10339b10-3cd1-4ac3-ac13-ec26728cb592" is in. Currently limited to 1
    # you can change this query to test different ones.
    print(ExecuteQuery('select * from test where PATIENT="10339b10-3cd1-4ac3-ac13-ec26728cb592" limit 1'))

if __name__ == "__main__":
    main()