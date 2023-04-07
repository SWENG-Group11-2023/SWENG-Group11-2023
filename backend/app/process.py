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
import math


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

                synset = best_synset_for_word(word)
                if synset is not None:
                    syns.append(synset.lemma_names()[0]) 


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


def process_pos(query, pos):
    split_query = query.split()
    words_in_pos = []
    for word in split_query:
        if pos_tag([word])[0][1][:2] == pos:
            words_in_pos.append(word)
    return words_in_pos


def best_synset_for_word(word):
    synsets = wordnet.synsets(word)
    if (len(synsets) > 0):
        return synsets[0]
    return None


def get_matching_descriptions(query, descriptions):
    matching_descriptions = []
    split_query = query.split()
    query_synsets = []

    for word in split_query:
        synset = best_synset_for_word(word)
        if synset is not None:
            query_synsets.append(synset)

    # determine the most similar description for the query as a whole
    overall_query_scores = np.zeros(len(descriptions), dtype=float)
    for i, description in enumerate(descriptions):
        for desc_word_synset in description[SYNONYMS_TITLE_JSON]:
            for query_synset in query_synsets:
                overall_query_scores[i] += wordnet.path_similarity(query_synset, best_synset_for_word(desc_word_synset))
        
        if (len(description[SYNONYMS_TITLE_JSON]) * len(query_synsets) != 0):
            overall_query_scores[i] /= len(description[SYNONYMS_TITLE_JSON]) * len(query_synsets)
        else:
            overall_query_scores[i] = 0
    
    # for each word in the query, determine whether any description is a great match
    for i, query_synset in enumerate(query_synsets):
        best_similarity_score = 0
        most_similar_description = None
        for description in descriptions:
            similarity = 0
            for desc_word_synset in description[SYNONYMS_TITLE_JSON]:
                similarity += wordnet.path_similarity(query_synset, best_synset_for_word(desc_word_synset))

            if len(description[SYNONYMS_TITLE_JSON]) > 0:
                similarity /= len(description[SYNONYMS_TITLE_JSON])
            else:
                similarity = 0

            if similarity > best_similarity_score:
                best_similarity_score = similarity
                most_similar_description = description
        
        if best_similarity_score >= DESCRIPTION_SIMILARITY_THRESHOLD and len(matching_descriptions) < 2:
            matching_descriptions.append(most_similar_description)
            query_synsets.remove(query_synset)  # remove the matched decription from the descriptions list so no other token matches

    if len(matching_descriptions) == 0:         # if no descriptions meet the similarity threshold, return the most similar
        return [descriptions[np.nanargmax(overall_query_scores)]]
    else:
        return matching_descriptions            # else return list of matching descriptions

    
def determine_query(query, descriptions):
    possible_metrics = ["list", "mean", "median", "mode", "maximum", "minimum", "range", "standard deviation"]

    score = np.zeros(len(possible_metrics), dtype=float)
    split_query = query.split()

    query_synsets = []
    for pos in pos_tag(split_query):
        if pos[1] == 'JJS' or pos[1] == 'RBS':
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

    if len(descriptions) > 1:
        second_parameter = get_second_parameter(split_query, query_synsets, descriptions[1])
    else:
        second_parameter = ""

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
    best_metric = possible_metrics[best_metric_index] if score[best_metric_index] >= METRIC_SIMILARITY_THRESHOLD else "list"
    print(f'Best statistical metric for the query: {best_metric}. Similarity score: {score[best_metric_index]}')

    best_description_key = descriptions[0]
    best_description = best_description_key["description"]

    metric_queries = {
        "list": f'select * from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter}',
        "mean": f'select AVG(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter}',
        "median": f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter} ORDER BY VALUE LIMIT 1 OFFSET (select COUNT(*) FROM {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter} / 2)',
        "mode": f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter} GROUP BY VALUE ORDER BY COUNT(CAST(VALUE AS REAL)) DESC LIMIT 1',
        "maximum": f'select MAX(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter}',
        "minimum": f'select MIN(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter}',
        "range": f'select MAX(CAST(VALUE AS REAL)) - MIN(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} where DESCRIPTION="{best_description}" {second_parameter}',
        "standard deviation": f'select SQRT(AVG(VALUE*VALUE) - AVG(CAST(VALUE AS REAL))*AVG(CAST(VALUE AS REAL))) from "{DB_TABLE_NAME}" where DESCRIPTION="{best_description}" {second_parameter}'
    }

    if score[best_metric_index] >= METRIC_SIMILARITY_THRESHOLD:
        metric_query = metric_queries[best_metric]
    else:
        metric_query = metric_queries["list"]

    return f'{metric_query}', best_metric


def get_second_parameter(split_query, query_synsets, description_key):
    description = description_key[DESCRIPTION_TITLE_JSON]

    boundary_value = None
    for token in split_query:
        try:
            boundary_value = float(token)
            break
        except:
            pass

    if boundary_value is None: return ""
    
    greater_synset = best_synset_for_word("greater")
    less_synset = best_synset_for_word("less")
    never_synset = best_synset_for_word("never")
    former_synset = best_synset_for_word("former")
    current_synset = best_synset_for_word("current")

    query = ""
    for query_synset in query_synsets:
        if wordnet.path_similarity(query_synset, greater_synset) >= SECOND_PARAMETER_SIMILARITY_THRESHOLD:
            query = (f'select DISTINCT PATIENT from {DB_TABLE_NAME} where DESCRIPTION="{description}" and CAST(VALUE AS REAL) > {boundary_value}')
            break

        elif wordnet.path_similarity(query_synset, less_synset) >= SECOND_PARAMETER_SIMILARITY_THRESHOLD:
            query = (f'select DISTINCT PATIENT from {DB_TABLE_NAME} where DESCRIPTION="{description}" and CAST(VALUE AS REAL) < {boundary_value}')
            break

        # TODO: support non-numerical values

    print(query)
    patients = execute_query(query)

    if len(patients) == 0:
        return ""

    patients_formatted = []
    for patient in patients:
        patients_formatted.append(format_single_value(patient))

    return f'and PATIENT in {str(patients_formatted).replace("[","(").replace("]",")")}'


def summarize(description, best_metric, units=None, type=None):
    metric = "the " + best_metric.capitalize() + " of " if best_metric.capitalize() != "List" else ""
    
    u = "" if units == None else " (" + units + ")"

    if (type=="text"):
        return f"Summary of {metric}" + description + " data (text data)"
    else:
        return f"Summary of {metric}" + description + " data" + u


def format_rows_for_graphing(rows, summary, best_metric, type):
    data = {"summary": summary, "values": [], "metrics": []}

    if (len(rows) != 1):
        if (type=="numeric"):
            numbers = []
            for row in rows:
                numbers.append(float(row[VALUE_COLUMN]))

            bins, labels = np.histogram(numbers, bins=10)
            for index, n in np.ndenumerate(bins):
                i = index[0]
                label = f"{round(labels[i], 1)},{round(labels[i+1], 1)}"
                data["values"].append({"name": label, "value": f"{n}"})

            n = np.array(numbers)

            data["metrics"] =  [
                {"average": f"{round(np.average(n), 3)}"},
                {"median": f"{round(np.median(n), 3)}"},
                {"max": f"{round(np.max(n), 3)}"},
                {"min": f"{round(np.min(n), 3)}"},
                {"range": f"{round(np.max(n) - np.min(n), 3)}"},
                {"standard deviation": f"{round(np.std(n), 3)}"},
            ]

            print(data["metrics"])

        elif(type == "text"):
            frequencies = dict()
            for row in rows:
                if row[VALUE_COLUMN] in frequencies:
                    frequencies[row[VALUE_COLUMN]] += 1
                else:
                    frequencies[row[VALUE_COLUMN]] = 1

            for label, value in frequencies.items():
                data["values"].append({"name": label, "value": f"{value}"})


        else:
            print("Error: Type needs to be text or numeric in format_rows_for_graphing")
            
    else:
        data["values"].append({"name": best_metric, "value": format_single_value(rows)})
    
    return data


def format_single_value(rows):
    return ''.join(str(rows[0]).replace(",","").replace("'","").replace("(","").replace(")",""))


def process_query(query):
    query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    query_without_stops = remove_stopwords(query_with_spaces)

    descriptions = descriptions_list()
    matching_descriptions = get_matching_descriptions(query_without_stops, descriptions)
    query, best_metric = determine_query(query_without_stops, matching_descriptions)
    rows = execute_query(query)
    
    best_description = matching_descriptions[0]
    
    if len(rows[0]) == 1:
        summary = summarize(best_description["description"], best_metric)
        data = format_rows_for_graphing(rows, summary, best_metric, "numeric")
    else:
        summary = summarize(best_description["description"], best_metric, rows[0][UNITS_COLUMN], rows[0][TYPE_COLUMN])
        data = format_rows_for_graphing(rows, summary, best_metric, rows[0][TYPE_COLUMN])
    
    return data


def download_to_csv(query):
    query_with_spaces = ''.join(' ' if letter == '+' else letter for letter in query).lower()
    query_without_stops = remove_stopwords(query_with_spaces)

    descriptions = descriptions_list()
    matching_descriptions = get_matching_descriptions(query_without_stops, descriptions)
    query, best_metric = determine_query(query_without_stops, matching_descriptions)
    rows = execute_query(query)

    if "select *" in query:
        stringified_rows = []
        for row in rows:
            s = ', '.join(list(row))
            stringified_rows.append(s)

        stringified_rows.insert(0, COLUMNS)
        return stringified_rows
    else:
        return [best_metric.capitalize(), format_single_value(rows[0])]


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

    data = process_query("give me the heart rates")
    print(data)