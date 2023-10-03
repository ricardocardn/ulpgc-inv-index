import pymongo
from document_handler import DocumentHandler
from mongo_db_manager import MongoDB

class Indexer:

    def __init__(self, MongoDB, datalake_path):
        self.mongoDB = MongoDB
        self.document_handler = DocumentHandler(datalake_path)


    def insert_all_documents(self):
        documents = self.document_handler.get_documents()

        for document_id, words in documents.items():
            if not self.mongoDB.is_inserted(document_id):
                self.mongoDB.insert_to_documents(document_id)
                self.insert_document(words, document_id)


    def insert_document(self, words, document_id):
        print(f"Inserting document {document_id}")
        for word in set(words):
            self.insert_word(word, document_id)
        

    def insert_word(self, word, document_id):
        inserted_doc_id = self.mongoDB.add_word(word, document_id)
        return inserted_doc_id