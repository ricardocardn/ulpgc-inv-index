import pymongo

import json

class Indexer:

    def __init__(self, mongoDB, document_handler):
        self.mongoDB = mongoDB
        self.document_handler = document_handler


    def insert_all_documents(self):
        documents = self.document_handler.get_documents()

        for document_id, words in documents.items():
            if not self.mongoDB.is_inserted(document_id):
                self.mongoDB.insert_to_documents(document_id)
                self.insert_document(words, document_id)


    def insert_documents(self, documents):
        for document_id in documents:
            if not self.mongoDB.is_inserted(document_id):
                self.mongoDB.insert_to_documents(document_id)
                words = self.document_handler.get_document(document_id)
                self.insert_document(words, document_id)


    def insert_document(self, words, document_id):
        print(f"Inserting document {document_id}")
        for word in set(words):
            self.mongoDB.add_word(word, document_id)