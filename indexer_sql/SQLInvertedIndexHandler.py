import time
from . import database_create
import os
from nltk import word_tokenize


class SQLInvertedIndexHandler:

    def insert_word_document(self, word, document_id):
        # Check if the word already exists in the Word table
        try:
            existing_word = database_create.Word.get(database_create.Word.word == word)
        except database_create.Word.DoesNotExist:
            # Word doesn't exist, create a new word entry
            existing_word = database_create.Word.create(word=word)

        # Check if the document already exists in the Document table
        try:
            existing_document = database_create.Document.get(database_create.Document.document_id == document_id)
        except database_create.Document.DoesNotExist:
            # Document doesn't exist, create a new document entry
            existing_document = database_create.Document.create(document_id=document_id)

        # Check if the word-document relation already exists
        try:
            existing_relation = database_create.WordDocumentAssociation.get(
                (database_create.WordDocumentAssociation.word == existing_word) &
                (database_create.WordDocumentAssociation.document == existing_document)
            )
            # Relation already exists, increment word_multiplicity by one
            existing_relation.word_multiplicity = str(int(existing_relation.word_multiplicity) + 1)
            existing_relation.save()
        except database_create.WordDocumentAssociation.DoesNotExist:
            # Relation doesn't exist, create a new relation entry
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

    def benchmark_inverted_index_of(self, document_list):
        start_time = time.time()
        self.inverted_index_of(document_list)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_time_formatted = f"{execution_time:.6f}"  # Format to 6 decimal places
        return execution_time_formatted

    # def get_documents():
    #    documents = os.listdir('./datalake/content')
    #    return documents
