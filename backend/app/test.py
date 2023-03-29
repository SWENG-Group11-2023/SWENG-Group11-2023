from sqlite import execute_query,create_db
from process import *
from constants import *
from nltk.corpus import wordnet

global descriptions

def test_execute_query():
    test_result = execute_query(f'select * from {DB_TABLE_NAME} where PATIENT="1d604da9-9a81-4ba9-80c2-de3375d59b40" limit 1')
    expected_result = [('2011-07-28T15:02:18Z', '1d604da9-9a81-4ba9-80c2-de3375d59b40', 'b85c339a-6076-43ed-b9d0-9cf013dec49d', 
                        '8302-2', 'Body Height', '181.0', 'cm', 'numeric')]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result = execute_query(f'select * from {DB_TABLE_NAME} where DESCRIPTION="Systolic Blood Pressure" limit 1')
    expected_result = [('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', 
                        '8480-6', 'Systolic Blood Pressure', '119.0', 'mm[Hg]', 'numeric')]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result = execute_query(f'select * from {DB_TABLE_NAME} where TYPE="numeric" limit 5')
    expected_result = [('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', 
                        '8302-2', 'Body Height', '193.3', 'cm', 'numeric'), ('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '72514-3', 'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
                        '2.0', '{score}', 'numeric'), ('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060',
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '29463-7', 'Body Weight', '87.8', 'kg', 'numeric'), ('2012-01-23T17:45:28Z',
                        '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '39156-5', 'Body Mass Index', '23.5',
                        'kg/m2', 'numeric'), ('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b',
                        '8462-4', 'Diastolic Blood Pressure', '82.0', 'mm[Hg]', 'numeric')]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"


def test_process_query():
    #test "list"
    test_result = process_query("give me a list of the potassium of patients")
    expected_result = format_rows_for_graphing(execute_query(f'select * from {DB_TABLE_NAME} where DESCRIPTION="Potassium"'))
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    #test "list"
    test_result = process_query("list the body height")
    expected_result = format_rows_for_graphing(execute_query(f'select * from {DB_TABLE_NAME} where DESCRIPTION="Body Height"'))
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    #test "list"
    test_result = process_query("give me a list of patients total cholesterol")
    expected_result = format_rows_for_graphing(execute_query(f'select * from {DB_TABLE_NAME} where DESCRIPTION="Total Cholesterol"'))
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "mean"
    test_result = process_query("give me the mean of the patients' respiratory rate")
    expected_result = "14.018164435946463"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "median"
    test_result = process_query("give me the median of the patients' respiratory rate")
    expected_result = "12.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "mode"
    test_result = process_query("give me the mode of the patients' respiratory rate")
    expected_result = "14.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "maximum"
    test_result = process_query("give me the maximum of the patients' respiratory rate")
    expected_result = "16.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "minimum"
    test_result = process_query("give me the minimum of the patients' respiratory rate")
    expected_result = "12.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "range"
    test_result = process_query("give me the range of the patients' respiratory rate")
    expected_result = "4.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "standard deviation"
    test_result = process_query("give me the standard deviation of the patients' respiratory rate")
    expected_result = "1.1529694844094023"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 


def test_format_rows_for_graphing():
    test_result = format_rows_for_graphing([('2011-07-28T15:02:18Z', '1d604da9-9a81-4ba9-80c2-de3375d59b40', 'b85c339a-6076-43ed-b9d0-9cf013dec49d',
                                             '8302-2', 'Body Height', '181.0', 'cm', 'numeric')])
    
    expected_result = [{'name': '1d604da9-9a81-4ba9-80c2-de3375d59b40', 'value': '181.0'}]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   


    test_result = format_rows_for_graphing([('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b',
                                             '8480-6', 'Systolic Blood Pressure', '119.0', 'mm[Hg]', 'numeric')])
    
    expected_result = [{'name': '034e9e3b-2def-4559-bb2a-7850888ae060', 'value': '119.0',}]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = format_rows_for_graphing([('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', 
                        '8302-2', 'Body Height', '193.3', 'cm', 'numeric'), ('2012-01-23 17:45:28', '034e9e3b-2def-4559-bb2a-7850888ae060', 
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '72514-3', 'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
                        '2.0', '{score}', 'numeric'), ('2012-01-23 17:45:28', '034e9e3b-2def-4559-bb2a-7850888ae060',
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '29463-7', 'Body Weight', '87.8', 'kg', 'numeric'), ('2012-01-23 17:45:28',
                        '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '39156-5', 'Body Mass Index', '23.5',
                        'kg/m2', 'numeric'), ('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b',
                        '8462-4', 'Diastolic Blood Pressure', '82.0', 'mm[Hg]', 'numeric')])
    
    expected_result = [{'name': '034e9e3b-2def-4559-bb2a-7850888ae060', 'value': '193.3'}, {'name': '034e9e3b-2def-4559-bb2a-7850888ae060',
                        'value': '2.0'}, {'name': '034e9e3b-2def-4559-bb2a-7850888ae060', 'value': '87.8',},
                        {'name': '034e9e3b-2def-4559-bb2a-7850888ae060', 'value': '23.5'}, {'name': '034e9e3b-2def-4559-bb2a-7850888ae060',
                        'value': '82.0'}]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"


def test_format_single_value():
    test_result = format_single_value([(14.018164435946463,)])
    expected_result = "14.018164435946463"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result = format_single_value([('16.0',)])
    expected_result = "16.0"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"


def test_determine_query():
    #test no metric
    query = "give patients respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select * from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "list"
    query = "give me a list of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select * from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"  

    #test "mean"
    query = "give me the mean of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select AVG(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "median"
    query = "give me the median of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}" ORDER BY VALUE LIMIT 1 OFFSET (select COUNT(*) FROM {DB_TABLE_NAME} WHERE DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}" / 2)'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "mode"
    query = "give me the mode of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select VALUE from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}" GROUP BY VALUE ORDER BY COUNT(VALUE) DESC LIMIT 1'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "average"
    query = "give the average respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select AVG(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "maximum"
    query = "give me the maximum of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select MAX(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "minimum"
    query = "give me the minimum of the patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select MIN(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "range"
    query = "give me the range of patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select MAX(VALUE) - MIN(VALUE) from {DB_TABLE_NAME} where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "standard deviation"
    query = "give me the standard deviation of patients' respiratory rate"
    best_description = closest_description(query, descriptions)
    test_result = determine_query(query, best_description[DESCRIPTION_TITLE_JSON])
    expected_result = f'select SQRT(AVG(VALUE*VALUE) - AVG(VALUE)*AVG(VALUE)) from "{DB_TABLE_NAME}" where DESCRIPTION="{best_description[DESCRIPTION_TITLE_JSON]}"'
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"


def test_closest_description():
    test_result = closest_description("weight", descriptions)[DESCRIPTION_TITLE_JSON]
    expected_result = "Body Weight"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = closest_description("height", descriptions)[DESCRIPTION_TITLE_JSON]
    expected_result = "Body Height"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = closest_description("pain severity", descriptions)[DESCRIPTION_TITLE_JSON]
    expected_result = "Pain severity - 0-10 verbal numeric rating [Score] - Reported"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 


def test_best_synset_for_word():
    test_result = best_synset_for_word("abcdefg")
    expected_result = None
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = best_synset_for_word("height")
    expected_result = (wordnet.synsets("height"))[0]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = best_synset_for_word("weight")
    expected_result = (wordnet.synsets("weight"))[0]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"      


def test_remove_stopwords():
    test_result = remove_stopwords("give me a list of the potassium of patients")
    expected_result = "give list potassium patients"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = remove_stopwords("list the body height")
    expected_result = "list body height"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = remove_stopwords("give me a list of patients total cholesterol")
    expected_result = "give list patients total cholesterol"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"


if __name__ == "__main__":
    create_db()
    descriptions_to_json()
    descriptions = descriptions_list()

    test_execute_query()
    test_process_query()
    test_format_rows_for_graphing()
    test_format_single_value()
    test_determine_query()
    test_closest_description()
    test_best_synset_for_word()
    test_remove_stopwords()
else:
    create_db()
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')
    descriptions_to_json()
    descriptions = descriptions_list()