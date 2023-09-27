import pymongo

class MongoDB:
    def __init__(self, port=27017, host="localhost", database="database", collection="index"):
        self.client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
        self.db = self.client[database]
        self.col = self.db[collection]


    def add_word(self, dict):
        query = {"word": dict["word"]}
        query_id = self.col.find_one(query)

        if query_id:
            for document in query_id["documents"]:
                if document["document_id"] == dict["documents"][0]["document_id"]:
                    document["positions"].append(dict["documents"][0]["positions"][0])
                    self.col.update_one(query, {"$set": {"documents": query_id["documents"]}})
                    return query_id["_id"]
            
            else:
                query_id["documents"].append(dict["documents"][0])
                self.col.update_one(query, {"$set": {"documents": query_id["documents"]}})
                return query_id["_id"]
            
        else:
            inserted_doc = self.col.insert_one(dict)
            return inserted_doc.inserted_id
    

    def find_query(self, word):
        query = {"word": word}
        result = self.col.find_one(query)
        return result