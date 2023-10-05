import pymongo
from .content_tokenizer import ContentTokenizer

class Indexer:

    def __init__(self, mongoDB, rute="datalake/content"):
        self.mongoDB = mongoDB
        self.contentTokenizer = ContentTokenizer(rute)


    def insert_documents(self, documents = None, top = None):
        documents = self.contentTokenizer.get_documents(documents, top)

        for document_id, words in documents.items():
            if not self.mongoDB.is_inserted(document_id):
                self.mongoDB.insert_to_documents(document_id)
                self.insert_document(words, document_id)
                

    def insert_document(self, words, document_id):
        print(f"Inserting document {document_id}")
        for word in set(words):
            self.mongoDB.add_word(word, document_id)


    def get_index(self):
        cursor = self.mongoDB.col.find({})
        inverted_index = dict()
        
        for word in cursor:
            inverted_index[word["word"]] = word["documents"]

        return inverted_index