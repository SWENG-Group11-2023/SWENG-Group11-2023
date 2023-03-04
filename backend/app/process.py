import os
import json
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from constants import *
from sqlite import execute_query
import numpy as np


def descriptions_to_json():
    description_tuples = execute_query(f'select distinct DESCRIPTION from {DB_TABLE_NAME}')
    descriptions = []

    #convert list of tuples to list of strings
    for description in description_tuples:
        descriptions.append(''.join(description))

    descriptions_json_string = json.dumps(descriptions)

    with open(DESCRIPTIONS, 'w') as descriptions_json_file:
        descriptions_json_file.write(descriptions_json_string)


def descriptions_list():
    with open (DESCRIPTIONS, 'r') as descriptions_json_file:
        return json.loads(descriptions_json_file.read())
    
def remove_stopwords(query):
    english_stopwords = stopwords.words("english")
    query_tokens = word_tokenize(query.lower())
    
    query_without_stops = []
    for word in query_tokens:
        if (word not in english_stopwords and word.isalpha()):
            query_without_stops.append(word)

    return ' '.join(query_without_stops)

def best_synset_for_word(word):
    synsets = wordnet.synsets(word)
    if (len(synsets) > 0):
        return synsets[0]
    return None



def closest_description(query, descriptions):
    score = np.zeros(len(descriptions), dtype=float)
    split_query = query.split()

    query_synsets = []
    for word in split_query:
        synset = best_synset_for_word(word)
        if synset is not None:
            query_synsets.append(synset)


    for i, description in enumerate(descriptions):
        
        description_words = remove_stopwords(description).split()
        description_words_synsets = []
        for word in description_words:
            synset = best_synset_for_word(word)

            if synset is not None:
                description_words_synsets.append(synset) 

        
        for desc_word_synset in description_words_synsets:

            for synset in query_synsets:
                score[i] += wordnet.path_similarity(synset, desc_word_synset)
        
        if (len(description_words_synsets) * len(query_synsets) != 0):
            score[i] /= len(description_words_synsets) * len(query_synsets)
        else:
            score[i] = 0
        

    # return score
    return descriptions[np.nanargmax(score)]

def format_rows_for_graphing(rows):
    data = []
    for row in rows:
        data.append({"name": row[PATIENT_ID_COLUMN], "value": row[VALUE_COLUMN]})

    return data

def process_query(query):
    nltk.data.path = [os.getcwd()] # keep, searches for corpora in current directory

    # query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    
    query_without_stops = remove_stopwords(query)
    descriptions = descriptions_list()
    best_description = closest_description(query_without_stops, descriptions)
    
    rows = execute_query(f'select * from {DB_TABLE_NAME} where DESCRIPTION="{best_description}"')
    data = format_rows_for_graphing(rows)
    return data


if __name__ == "__main__":
    nltk.data.path = [os.getcwd()]
    # use this to download
    # nltk.download("some-package", download_dir=os.getcwd)   

    #descriptions_to_json() #uncomment to generate JSON file containing all patient descriptions

    data = process_query("give me a list of the patients' status of HIV")
    print(data)

    