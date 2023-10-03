import pymongo

class MongoDB:
    """
    MongoDB class to manage the connection to the database and queries
    """

    def __init__(self, port=27017, host="localhost", database="database", collection="index"):
        """ Constructor of the class
        Establish the connection to the database
        :param port: Port of the database
        :param host: Host of the database
        :param database: Name of the database
        :param collection: Name of the collection
        """

        self.client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
        self.db = self.client[database]
        self.col = self.db[collection]


    def add_word(self, word, id):
        """ Add a word to the collection
        :param dict: Dictionary with the word and the document
        :return: The id of the inserted document
        """

        # Check if the word already exists
        query = {"word": dict["word"]}
        query_id = self.col.find_one(query)

        if query_id:
            if self.inserted(id):
            query_id["documents"].append(dict["documents"][0])
            self.col.update_one(query, {"$set": {"documents": query_id["documents"]}})
            return query_id["_id"]
            
        else:
            # If the word doesn't exist, add it to the collection
            inserted_doc = self.col.insert_one(dict)
            return inserted_doc.inserted_id
    

    def find_query(self, word):
        """ Find a word in the collection
        :param word: Word to find
        :return: The word document
        """

        # Find the word in the collection
        query = {"word": word}
        result = self.col.find_one(query)
        return result