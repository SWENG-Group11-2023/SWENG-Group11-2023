import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sqlite import *


def descriptions_to_json():
    description_tuples = execute_query(f'select distinct DESCRIPTION from {DB_TABLE_NAME}')
    descriptions = []

    #convert list of tuples to list of strings
    for description in description_tuples:
        descriptions.append(''.join(description))

    descriptions_json_string = json.dumps(descriptions)

    with open('descriptions.json', 'w') as descriptions_json_file:
        descriptions_json_file.write(descriptions_json_string)


def descriptions_list():
    with open ('descriptions.json', 'r') as descriptions_json_file:
        return json.loads(descriptions_json_file.read())


def process_query(query):
    nltk.data.path = [os.getcwd()] # keep, searches for corpora in current directory

    # query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    
    english_stopwords = stopwords.words("english")
    query_tokens = word_tokenize(query.lower())
    
    query_without_stops = []
    for word in query_tokens:
        if (word not in english_stopwords and word.isalpha()):
            query_without_stops.append(word)

    return query_without_stops


if __name__ == "__main__":
    # if using nltk.download(), set download_dir=os.getcwd() as parameter
    
    #descriptions_to_json() #uncomment to generate JSON file containing all patient descriptions

    answer = process_query("What is the average body height?")
    print(answer)
    