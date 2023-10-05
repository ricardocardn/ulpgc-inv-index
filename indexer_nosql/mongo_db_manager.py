import pymongo

class MongoDB:
    def __init__(self, port=27017, host="localhost", database="database", collection="index", doc_collection="document_index"):
        self.client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
        self.db = self.client[database]
        self.col = self.db[collection]
        self.documents_col = self.db[doc_collection]


    def add_word(self, word, document_id):
        query = {"word": word}
        query_id = self.col.find_one(query)

        if query_id:
            query_id["documents"].append(document_id)
            self.col.update_one(query, {"$set": {"documents": query_id["documents"]}})
            return query_id["_id"]
            
        else:
            dict = {"word": word, "documents": [document_id]}
            inserted_doc = self.col.insert_one(dict)
            return inserted_doc.inserted_id
        

    def insert_to_documents(self, id):
        dict = {"document": id}
        inserted_doc = self.documents_col.insert_one(dict)
        return inserted_doc.inserted_id


    def is_inserted(self, id):
        query = {"document": id}
        result = self.documents_col.find_one(query)
        
        return True if result else False


    def find_query(self, word):
        query = {"word": word}
        result = self.col.find_one(query)
        return result


    def get_content(self):
        cursor = self.col.find({})
        inverted_index = dict()
        
        for word in cursor:
            inverted_index[word["word"]] = word["documents"]

        return inverted_index
    

    def delete_document(self, id):
        self.delete_from_documents(id)
        self.delete_document_from_word_index(id)
    

    def delete_from_documents(self, id):
        query = {"document": id}
        self.documents_col.delete_many(query)


    def delete_document_from_word_index(self, id):
        query = {"documents": id}
        self.col.delete_many(query)


    def clean_db(self):
        self.col.delete_many({})
        self.documents_col.delete_many({})