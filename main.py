from mongodb.mongo_db_manager import MongoDB
from mongodb.inverted_index import InvertedIndexHandler
from mongodb.inverted_index_creator import InvertedIndexCreator

if __name__ == '__main__':
    mongoDB = MongoDB()
    inverted_index_handler = InvertedIndexHandler(mongoDB)
    inverted_index_creator = InvertedIndexCreator(mongoDB, inverted_index_handler)

    inverted_index_creator.insert_all_documents()