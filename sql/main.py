import os

import nltk
from nltk import word_tokenize

import datalake_builder as datalake_builder
from InvertedIndexHandler import InvertedIndexHandler
from datalake_builder import parse_files, normalize
from datalake_builder import get_language
from nltk.corpus import stopwords, words


def is_english_word(word):
    return word.lower() in set(words.words())
def split_document_to_words(document_id, metadata_id):
    with open(os.path.join('datalake/content', document_id), encoding="utf-8") as f:
        content_text = f.read()
    with open(os.path.join('datalake/metadata', metadata_id), encoding="utf-8") as f:
        metadata_text = f.read()
    english_stopwords = set(stopwords.words(get_language(metadata_text).lower()))
    document = word_tokenize(content_text)
    filtered_words = [word for word in document if word not in english_stopwords]
    return filtered_words
def inverted_index_index_of():
    iih = InvertedIndexHandler()

    document_list = get_documents("content")
    metadata_list = get_documents("metadata")

    for document_id, metadata_id in zip(document_list, metadata_list):
        words = split_document_to_words(document_id, metadata_id)
        for word in words:
            iih.insert_word_document(word, document_id)

def get_documents(type):
    documents = os.listdir('datalake/' + str(type))

    return documents



def main():
    parse_files()
    normalize(get_documents("content"))
    inverted_index_index_of()


if __name__ == "__main__":
    main()