import os
import re

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords, words


def parse_files():
    for filename in os.listdir('datalake/books'):
        name = filename.split('.txt')[0].split('_')[2]

        with open(os.path.join('datalake/books', filename), encoding="utf-8") as f:
            text = f.read()

            text = text.split('***')

            with open(os.path.join('datalake/metadata', name + '.metadata'), 'w', encoding="utf-8") as f:
                f.write(text[0] + '***' + text[1] + '***')
                f.write('\n')
                f.write(text[-1])

            with open(os.path.join('datalake/content', name + '.txt'), 'w', encoding="utf-8") as f:
                f.write(text[2].lower())


def get_language(document):
    pattern=r"Language:\s(\w+)"
    language=re.search(pattern, document)
    return language.group(1)


def remove_non_alphanumeric_characters(text):
    processed_text = re.sub(r'[^A-Za-z\s]', '', text)
    return processed_text


def remove_spaces_oneword(text):
    text_without_single_letters  = ' '.join([word for word in text.split() if len(word) > 1])
    normalised_text = ' '.join(text_without_single_letters .split())

    return normalised_text


def normalize(documents, metadata):
    nltk.download('stopwords')
    nltk.download('punkt')

    for doc, met in zip(documents,metadata):
        with open(os.path.join("datalake/content", doc), 'r', encoding='utf-8') as file:
            text = file.read()
            processed_text = remove_non_alphanumeric_characters(text)
            processed_text = remove_spaces_oneword(processed_text)

        with open(os.path.join('datalake/metadata', met), encoding="utf-8") as f:
            metadata_text = f.read()

        language = get_language(metadata_text)
        language_stopwords = set(stopwords.words(language.lower()))
        document = word_tokenize(processed_text)
        filtered_words = [word for word in document if word not in language_stopwords]

        with open(os.path.join("datalake/content", doc), 'w', encoding='utf-8') as output:
            output.write(' '.join(filtered_words))


def create_datalake():
    parse_files()
    normalize(os.listdir('datalake/content'), os.listdir('datalake/metadata'))
