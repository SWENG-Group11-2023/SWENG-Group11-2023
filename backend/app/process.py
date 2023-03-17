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


def best_query_metric(query):
    possible_metrics = ["list", "average", "maximum", "minimum"]

    score = np.zeros(len(possible_metrics), dtype=float)
    split_query = query.split()

    query_synsets = []
    for word in split_query:
        synset = best_synset_for_word(word)
        if synset is not None:
            query_synsets.append(synset)

    metric_words_synsets = []
    for metric in possible_metrics:
        synset = best_synset_for_word(metric)

        if synset is not None:
            metric_words_synsets.append(synset) 

    for i, metric_word_synset in enumerate(metric_words_synsets):

        for query_synset in query_synsets:
            score[i] += wordnet.path_similarity(query_synset, metric_word_synset)
    
        if (len(query_synsets) != 0):
            score[i] /= len(query_synsets)
        else:
            score[i] = 0
        
    best_metric_index = np.nanargmax(score)

    if score[best_metric_index] >= METRIC_SIMILARITY_THRESHOLD:
        metric_functions = {"list": "*", "average": "AVG(VALUE)", "maximum": "MAX(VALUE)", "minimum": "MIN(VALUE)"}
        metric_function = metric_functions[possible_metrics[best_metric_index]]

        return(f'{metric_function}')
    
    return("*")
    

def format_rows_for_graphing(rows):
    data = []
    for row in rows:
        data.append({"name": row[PATIENT_ID_COLUMN], "value": row[VALUE_COLUMN]})

    return data


def format_single_value(rows):
    return ''.join(str(rows[0]).replace(",","").replace("'",""))


def process_query(query):
    nltk.data.path = [os.getcwd()] # keep, searches for corpora in current directory

    # query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    
    query_without_stops = remove_stopwords(query)
    descriptions = descriptions_list()
    best_description = closest_description(query_without_stops, descriptions)
    query_metric = best_query_metric(query_without_stops)

    rows = execute_query(f'select {query_metric} from {DB_TABLE_NAME} where DESCRIPTION="{best_description}"')
    data = format_rows_for_graphing(rows) if query_metric == "*" else format_single_value(rows)

    return data


if __name__ == "__main__":
    nltk.data.path = [os.getcwd()]
    # use this to download
    # nltk.download("some-package", download_dir=os.getcwd())   

    #descriptions_to_json() #uncomment to generate JSON file containing all patient descriptions

    data = process_query("give me the mean of the patients' respiratory rate")
    print(data)

    