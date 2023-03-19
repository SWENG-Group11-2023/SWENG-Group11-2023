import csv
import sqlite3
from constants import *
import os
import shutil
import urllib.request
import zipfile

def create_db():
    if 'production.db' not in os.listdir():
        # Path to the zip file
        zip_path = "synthea_sample_data_csv_apr2020.zip"

        # Download the zip file
        urllib.request.urlretrieve(DATA_URL, zip_path)

        # unzip the file to current directory then remove it
        # since it is zip file will create the ./csv/ folder
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall()
        # removing downloaded zip file
        os.remove(zip_path)

        # create database from downloaded zip file and removes associated files once done
        create_table()
        shutil.rmtree('./csv/')
    else:
        print("DB already exists")


def execute_query(query):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()
    cursor.close()
    connection.close()
    return result

def create_table():
    """
    Creates the production database
    """
    try:
        # importing csv and extracting the data
        with open(DATA_CSV,'r') as file:
            reader = csv.DictReader(file)
            observations = [(i['DATE'],i['PATIENT'],i['ENCOUNTER'],i['CODE'],i['DESCRIPTION'],
                i['VALUE'],i['UNITS'],i['TYPE']) for i in reader]
            
        # connect to database. Will create DB_PATH if it does not yet exist
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
        cursor.executemany(f'INSERT INTO {DB_TABLE_NAME} (DATE,PATIENT,ENCOUNTER,CODE,DESCRIPTION,VALUE,UNITS,TYPE) VALUES (?,?,?,?,?,?,?,?)',observations)
        connection.commit()
        cursor.close()
        connection.close()

    except sqlite3.Error as error:
        print(f"Error: {error}")

def test_db():
    print(execute_query(f'select * from {DB_TABLE_NAME} where PATIENT="10339b10-3cd1-4ac3-ac13-ec26728cb592" limit 1'))

if __name__ == "__main__":
    create_table()
    test_db()