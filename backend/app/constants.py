# constants to be used throughout the project to have easy change of file names etc
DB_PATH = './production.db'
DATA_CSV = './csv/observations.csv'
DESCRIPTIONS = './descriptions.json'
DB_TABLE_NAME = 'main_table'
PATIENT_ID_COLUMN = 1
VALUE_COLUMN = 5
UNITS_COLUMN = 6
TYPE_COLUMN = 7
METRIC_SIMILARITY_THRESHOLD = 0.17
DESCRIPTION_SIMILARITY_THRESHOLD = 0.5
SECOND_PARAMETER_SIMILARITY_THRESHOLD = 0.3
DATA_URL = "https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip"

DESCRIPTION_TITLE_JSON = "description"
SYNONYMS_TITLE_JSON = "synonyms"
COLUMNS = "DATE, PATIENT, ENCOUNTER, CODE, DESCRIPTION, VALUE, UNITS, TYPE"