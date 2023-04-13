from sqlite import execute_query,create_db
from process import *
from constants import *
from nltk.corpus import wordnet

global descriptions

def test_execute_query():
    test_result = execute_query(f'select * from {DB_TABLE_NAME} WHERE PATIENT="1d604da9-9a81-4ba9-80c2-de3375d59b40" limit 1')
    expected_result = [('2011-07-28T15:02:18Z', '1d604da9-9a81-4ba9-80c2-de3375d59b40', 'b85c339a-6076-43ed-b9d0-9cf013dec49d', 
                        '8302-2', 'Body Height', '181.0', 'cm', 'numeric')]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result = execute_query(f'select * from {DB_TABLE_NAME} WHERE DESCRIPTION="Systolic Blood Pressure" limit 1')
    expected_result = [('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', 
                        '8480-6', 'Systolic Blood Pressure', '119.0', 'mm[Hg]', 'numeric')]
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result = execute_query(f'select * from {DB_TABLE_NAME} WHERE TYPE="numeric" limit 5')
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
    test_result = str(process_query("give me a list of the potassium of patients"))
    expected_result = format("{'summary': 'Summary of Potassium data (mmol/L)', 'values': [{'name': '3.7,3.8', 'value': '599'}, {'name': '3.8,4.0', 'value': '449'}, " +
                             "{'name': '4.0,4.2', 'value': '865'}, {'name': '4.2,4.3', 'value': '420'}, {'name': '4.3,4.4', 'value': '868'}, " +
                             "{'name': '4.4,4.6', 'value': '454'}, {'name': '4.6,4.8', 'value': '855'}, {'name': '4.8,4.9', 'value': '440'}, " +
                             "{'name': '4.9,5.0', 'value': '870'}, {'name': '5.0,5.2', 'value': '695'}], 'metrics': [{'average': '4.461'}, {'median': '4.5'}, " +
                             "{'max': '5.2'}, {'min': '3.7'}, {'range': '1.5'}, {'standard deviation': '0.436'}]}")
    assert test_result == expected_result, f"Got wrong result, expected is: \n{expected_result}, actual is \n\n\n\n{test_result}"   

    #test "list"
    test_result = str(process_query("list the body height"))
    expected_result = format("{'summary': 'Summary of Body Height data (cm)', 'values': [{'name': '45.1,60.5', 'value': '296'}, {'name': '60.5,75.8', 'value': '462'}, " +
                             "{'name': '75.8,91.2', 'value': '476'}, {'name': '91.2,106.5', 'value': '448'}, {'name': '106.5,121.9', 'value': '339'}, " +
                             "{'name': '121.9,137.3', 'value': '424'}, {'name': '137.3,152.6', 'value': '611'}, {'name': '152.6,168.0', 'value': '4342'}, " +
                             "{'name': '168.0,183.3', 'value': '4265'}, {'name': '183.3,198.7', 'value': '889'}], 'metrics': [{'average': '153.85'}, {'median': '165.0'}, " +
                             "{'max': '198.7'}, {'min': '45.1'}, {'range': '153.6'}, {'standard deviation': '33.72'}]}")
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    #test "list"
    test_result = str(process_query("give me a list of patients total cholesterol"))
    expected_result = format("{'summary': 'Summary of Total Cholesterol data (mg/dL)', 'values': [{'name': '150.0,165.4', 'value': '640'}, " + 
                             "{'name': '165.4,180.8', 'value': '1454'}, {'name': '180.8,196.2', 'value': '1380'}, {'name': '196.2,211.6', 'value': '866'}, " +
                             "{'name': '211.6,227.0', 'value': '433'}, {'name': '227.0,242.4', 'value': '352'}, {'name': '242.4,257.8', 'value': '109'}, " +
                             "{'name': '257.8,273.2', 'value': '16'}, {'name': '273.2,288.6', 'value': '5'}, {'name': '288.6,304.0', 'value': '9'}], " +
                             "'metrics': [{'average': '190.484'}, {'median': '186.9'}, {'max': '304.0'}, {'min': '150.0'}, {'range': '154.0'}, {'standard deviation': '23.325'}]}")
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "mean"
    test_result = str(process_query("give me the mean of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Mean of Respiratory rate data', 'values': [{'name': 'mean', 'value': '14.018164435946463'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "median"
    test_result = str(process_query("give me the median of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Median of Respiratory rate data', 'values': [{'name': 'median', 'value': '14.0'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "maximum"
    test_result = str(process_query("give me the maximum of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Maximum of Respiratory rate data', 'values': [{'name': 'maximum', 'value': '16.0'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    #test "minimum"
    test_result = str(process_query("give me the minimum of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Minimum of Respiratory rate data', 'values': [{'name': 'minimum', 'value': '12.0'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "range"
    test_result = str(process_query("give me the range of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Range of Respiratory rate data', 'values': [{'name': 'range', 'value': '4.0'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 

    #test "standard deviation"
    test_result = str(process_query("give me the standard deviation of the patients' respiratory rate"))
    expected_result = "{'summary': 'Summary of the Standard deviation of Respiratory rate data', 'values': [{'name': 'standard deviation', 'value': '1.1529694844094023'}], 'metrics': []}"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}" 


#TODO
def test_summarize(): 
    assert(1)


#TODO
def test_most_similar_value():
    assert(1)


#TODO
def test_get_second_parameter():
    assert(1)


#TODO
def test_process_pos():
    assert(1)


def test_format_rows_for_graphing():
    test_result = str(format_rows_for_graphing([('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', 
                        '8302-2', 'Body Height', '193.3', 'cm', 'numeric'), ('2012-01-23 17:45:28', '034e9e3b-2def-4559-bb2a-7850888ae060', 
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '72514-3', 'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
                        '2.0', '{score}', 'numeric'), ('2012-01-23 17:45:28', '034e9e3b-2def-4559-bb2a-7850888ae060',
                        'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '29463-7', 'Body Weight', '87.8', 'kg', 'numeric'), ('2012-01-23 17:45:28',
                        '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b', '39156-5', 'Body Mass Index', '23.5',
                        'kg/m2', 'numeric'), ('2012-01-23T17:45:28Z', '034e9e3b-2def-4559-bb2a-7850888ae060', 'e88bc3a9-007c-405e-aabc-792a38f4aa2b',
                        '8462-4', 'Diastolic Blood Pressure', '82.0', 'mm[Hg]', 'numeric')], "Summary of Test Data", "list", "numeric"))

    expected_result = format("{'summary': 'Summary of Test Data', 'values': [{'name': '2.0,21.1', 'value': '1'}, {'name': '21.1,40.3', 'value': '1'}, " +
                            "{'name': '40.3,59.4', 'value': '0'}, {'name': '59.4,78.5', 'value': '0'}, {'name': '78.5,97.6', 'value': '2'}, " +
                            "{'name': '97.6,116.8', 'value': '0'}, {'name': '116.8,135.9', 'value': '0'}, {'name': '135.9,155.0', 'value': '0'}, " +
                            "{'name': '155.0,174.2', 'value': '0'}, {'name': '174.2,193.3', 'value': '1'}], 'metrics': [{'average': '77.72'}, " +
                            "{'median': '82.0'}, {'max': '193.3'}, {'min': '2.0'}, {'range': '191.3'}, {'standard deviation': '66.561'}]}")
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
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = 'select * from main_table WHERE DESCRIPTION="Respiratory rate"'
    expected_result2 = "list"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "list"
    query = "give me a list of the patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = 'select * from main_table WHERE DESCRIPTION="Respiratory rate"'
    expected_result2 = "list"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "mean"
    query = "give me the mean of the patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select AVG(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "mean"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "median"
    query = "give me the median of the patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select VALUE from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}" ORDER BY CAST(VALUE AS REAL) LIMIT 1 OFFSET (select COUNT(*) FROM {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}") / 2'
    expected_result2 = "median" 
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "average"
    query = "give the average respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select AVG(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "mean"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "maximum"
    query = "give me the maximum of the patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select MAX(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "maximum"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "minimum"
    query = "give me the minimum of the patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select MIN(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "minimum"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "range"
    query = "give me the range of patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select MAX(CAST(VALUE AS REAL)) - MIN(CAST(VALUE AS REAL)) from {DB_TABLE_NAME} WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "range"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"

    #test "standard deviation"
    query = "give me the standard deviation of patients' respiratory rate"
    matching_descriptions = get_matching_descriptions(query, descriptions)
    test_result1, test_result2 = determine_query(query, matching_descriptions)
    expected_result1 = f'select SQRT(AVG(VALUE*VALUE) - AVG(CAST(VALUE AS REAL))*AVG(CAST(VALUE AS REAL))) from "{DB_TABLE_NAME}" WHERE DESCRIPTION="{matching_descriptions[0][DESCRIPTION_TITLE_JSON]}"'
    expected_result2 = "standard deviation"    
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}"


def test_get_matching_descriptions():
    test_result = get_matching_descriptions("weight", descriptions)[0][DESCRIPTION_TITLE_JSON]
    expected_result = "Body Weight"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = get_matching_descriptions("height", descriptions)[0][DESCRIPTION_TITLE_JSON]
    expected_result = "Body Height"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"   

    test_result = get_matching_descriptions("pain severity", descriptions)[0][DESCRIPTION_TITLE_JSON]
    expected_result = "Pain severity - 0-10 verbal numeric rating [Score] - Reported"
    assert test_result == expected_result, f"Got wrong result, expected is: {expected_result}, actual is {test_result}"

    test_result1 = get_matching_descriptions("Give me the maximum weight of patients with heart rate less than 70.", descriptions)[0][DESCRIPTION_TITLE_JSON]
    test_result2 = get_matching_descriptions("Give me the maximum weight of patients with heart rate less than 70.", descriptions)[1][DESCRIPTION_TITLE_JSON]
    expected_result1 = "Body Weight"
    expected_result2 = "Heart rate"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result1}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result2}, actual is {test_result2}" 

    test_result1 = get_matching_descriptions("What is the mean blood pressure of patients whose housing status is homeless?", descriptions)[0][DESCRIPTION_TITLE_JSON]
    test_result2 = get_matching_descriptions("What is the mean blood pressure of patients whose housing status is homeless?", descriptions)[1][DESCRIPTION_TITLE_JSON]
    expected_result1 = "Diastolic Blood Pressure"
    expected_result2 = "Housing status"
    assert test_result1 == expected_result1, f"Got wrong result, expected is: {expected_result1}, actual is {test_result2}"
    assert test_result2 == expected_result2, f"Got wrong result, expected is: {expected_result1}, actual is {test_result2}" 


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
    test_summarize()
    test_most_similar_value()
    test_get_second_parameter()
    test_process_pos()
    test_format_rows_for_graphing()
    test_format_single_value()
    test_determine_query()
    test_get_matching_descriptions()
    test_best_synset_for_word()
    test_remove_stopwords()
    print("\nAll tests passed successfully.")
else:
    create_db()
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')
    descriptions_to_json()
    descriptions = descriptions_list()