import time
from . import database_create
import os
from nltk import word_tokenize


class SQLInvertedIndexHandler:

    def insert_word_document(self, word, document_id):
        try:
            existing_word = database_create.Word.get(database_create.Word.word == word)
        except database_create.Word.DoesNotExist:
            existing_word = database_create.Word.create(word=word)

        try:
            existing_document = database_create.Document.get(database_create.Document.document_id == document_id)
        except database_create.Document.DoesNotExist:
            existing_document = database_create.Document.create(document_id=document_id)

        try:
            existing_relation = database_create.WordDocumentAssociation.get(
                (database_create.WordDocumentAssociation.word == existing_word) &
                (database_create.WordDocumentAssociation.document == existing_document)
            )
            existing_relation.word_multiplicity = str(int(existing_relation.word_multiplicity) + 1)
            existing_relation.save()
        except database_create.WordDocumentAssociation.DoesNotExist:
            database_create.WordDocumentAssociation.create(
                word=existing_word,
                document=existing_document,
                word_multiplicity="1"
            )

    def inverted_index_of(self, document_list):
        for document_id in document_list:
            with open(os.path.join("datalake/content", document_id), 'r', encoding='utf-8') as file:
                text = file.read()
                words = word_tokenize(text)
                for word in words:
                    self.insert_word_document(word, document_id)
