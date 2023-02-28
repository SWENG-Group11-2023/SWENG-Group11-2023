import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



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

    answer = process_query("What is the average body height?")
    print(answer)
