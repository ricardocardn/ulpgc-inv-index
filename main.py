import os

import nltk
from nltk import word_tokenize
from InvertedIndexHandler import InvertedIndexHandler
from datalake_builder import parse_files
from nltk.corpus import stopwords, words


def is_english_word(word):
    return word.lower() in set(words.words())
def split_document_to_words(document):
    with open(os.path.join('data', document), encoding="utf-8") as f:
        text = f.read()
    english_stopwords = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in english_stopwords]
    return filtered_words
def inverted_index_index_of(document_list):
    iih = InvertedIndexHandler()

    for document_id in document_list:
        words = split_document_to_words(document_id)
        for word in words:
            iih.insert_word_document(word, document_id)

def get_documents():
    documents = os.listdir('data')
    parsed_names = []
    for document in documents:
        parsed_names.append(document.replace(".txt", ""))
    return documents

def main():
    parse_files()
    inverted_index_index_of(get_documents())


if __name__ == "__main__":
    main()