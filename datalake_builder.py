import os
import re


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
    # Uses a regular expression to remove non-alphabetic characters and numbers
    processed_text = re.sub(r'[^A-Za-z\s]', '', text)
    return processed_text

def normalize(documents):
    # Process and overwrite each file in the same input directory
    for document in documents:
        with open(os.path.join("datalake/content", document), 'r', encoding='utf-8') as file:
            text = file.read()
            processed_text = remove_non_alphanumeric_characters(text)

            # Overwrite the original file with the processed text
            with open(os.path.join("datalake/content", document), 'w', encoding='utf-8') as output:
                output.write(processed_text)

def remove_stop_words():
    pass