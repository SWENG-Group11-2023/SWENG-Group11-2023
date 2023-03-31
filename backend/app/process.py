import os
import json
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from constants import *
from sqlite import execute_query,create_db
import numpy as np
import re


def descriptions_to_json(dev=False):

    if not os.path.exists(DESCRIPTIONS) or dev:


        description_tuples = execute_query(f'select distinct DESCRIPTION from {DB_TABLE_NAME}')
        descriptions = []

        #convert list of tuples to list of strings
        for description in description_tuples:
            descriptions.append(''.join(description))

        descriptions_with_syns = []

        for desc in descriptions:
            d = remove_stopwords(desc).split()
            syns = []
            for word in d:

                # synsets = wordnet.synsets(word)
                # for synset in synsets:
                #     if synset is not None:
                #         syns.append(synset.lemma_names()[0])

                synset = best_synset_for_word(word)
                if synset is not None:
                    syns.append(synset.lemma_names()[0]) 

            # syns = list(set(syns))

            dict = {DESCRIPTION_TITLE_JSON: desc, SYNONYMS_TITLE_JSON: syns}
            descriptions_with_syns.append(dict)

        descriptions_json_string = json.dumps(descriptions_with_syns, indent=2)

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
        if (word not in english_stopwords):
            query_without_stops.append(word)

    q = ' '.join(query_without_stops)
    return re.sub('[^0-9a-zA-Z]+', ' ', q)


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
        for desc_word_synset in description[SYNONYMS_TITLE_JSON]:

            for synset in query_synsets:
                score[i] += wordnet.path_similarity(synset, best_synset_for_word(desc_word_synset))
        
        if (len(description[SYNONYMS_TITLE_JSON]) * len(query_synsets) != 0):
            score[i] /= len(description[SYNONYMS_TITLE_JSON]) * len(query_synsets)
        else:
            score[i] = 0
        

    # return score
    return descriptions[np.nanargmax(score)]



def determine_query(query, description):
    possible_metrics = ["list", "mean", "median", "mode", "maximum", "minimum", "range", "standard deviation"]

    score = np.zeros(len(possible_metrics), dtype=float)
    split_query = query.split()

    query_synsets = []
    for pos in pos_tag(split_query):
        if pos[1] == 'JJS':
            synsets = wordnet.synsets(wordnet.synsets(pos[0])[0].name().split('.')[0])
            for syn in synsets:
                for word in syn.lemmas():
                    if word.name() == 'high' or word.name() == 'big':
                        query_synsets.append(wordnet.synsets('maximum')[0])
                    if word.name() == 'low' or word.name() == 'small':
                        query_synsets.append(wordnet.synsets('minimum')[0])
                        
    for word in split_query:
        synset = best_synset_for_word(word)
        if synset is not None:
            query_synsets.append(synset)

    metric_synsets = []
    for metric in possible_metrics:
        split_metric = metric.split()
        word_synsets = []
        for word in split_metric:
            synset = best_synset_for_word(word)

            if synset is not None:
                word_synsets.append(synset)

        metric_synsets.append(word_synsets)

    for i, metric_word_synsets in enumerate(metric_synsets):

        for query_synset in query_synsets:
            for metric_word_synset in metric_word_synsets:
                score[i] += wordnet.path_similarity(query_synset, metric_word_synset)
    
        if (len(metric_word_synsets) * len(query_synsets) != 0):
            score[i] /= len(metric_word_synsets) * len(query_synsets)
        else:
            score[i] = 0
        
    best_metric_index = np.nanargmax(score)
    best_metric = possible_metrics[best_metric_index]
    print(f'Best statistical metric for the query: {best_metric}. Similarity score: {score[best_metric_index]}')

    if score[best_metric_index] >= METRIC_SIMILARITY_THRESHOLD:
        metric_queries = {
            "list": f'select * from {DB_TABLE_NAME} where DESCRIPTION="{description}"',
            "mean": f'select AVG(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{description}"',
            "median": f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{description}" ORDER BY VALUE LIMIT 1 OFFSET (select COUNT(*) FROM {DB_TABLE_NAME} WHERE DESCRIPTION="{description}" / 2)',
            "mode": f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{description}" GROUP BY VALUE ORDER BY COUNT(VALUE) DESC LIMIT 1',
            "maximum": f'select MAX(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{description}"',
            "minimum": f'select MIN(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{description}"',
            "range": f'select MAX(VALUE) - MIN(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{description}"',
            "standard deviation": f'select SQRT(AVG(VALUE*VALUE) - AVG(VALUE)*AVG(VALUE)) from "{DB_TABLE_NAME}" where DESCRIPTION="{description}"'
        }

        metric_query = metric_queries[best_metric]

        return(f'{metric_query}')
    
    return(f'select * from {DB_TABLE_NAME} where DESCRIPTION="{description}"')
    

def format_rows_for_graphing(rows):
    data = []
    for row in rows:
        data.append({"name": row[PATIENT_ID_COLUMN], "value": row[VALUE_COLUMN]})

    return data


def format_single_value(rows):
    return ''.join(str(rows[0]).replace(",","").replace("'","").replace("(","").replace(")",""))


def process_query(query):

    # query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    
    query_without_stops = remove_stopwords(query)
    descriptions = descriptions_list()
    best_description = closest_description(query_without_stops, descriptions)
    query = determine_query(query_without_stops, best_description[DESCRIPTION_TITLE_JSON])

    rows = execute_query(query)
    data = format_rows_for_graphing(rows) if "select *" in query else format_single_value(rows)

    return data


if __name__ == "__main__":
    # if db does not exists creates it
    create_db()

    # generates the descriptions.json file
    descriptions_to_json()

    # automatically checks if nltk modules are up to date downloads if necessary
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')

    data = process_query("give me the standard deviation of respiratory rate")
    print(data)

    
