#from mongodb.mongo_db_manager import MongoDB
#from mongodb.inverted_index_handler import InvertedIndexHandler
#from mongodb.local_inverted_index import LocalInvertedIndex
#from mongodb.document_handler import DocumentHandler
from datalake_builder import create_datalake

import time

if __name__ == '__main__':

    create_datalake()
    #add_to_mongo()

    # datalake 
    """
    mongoDB = MongoDB()
    inverted_index_handler = InvertedIndexHandler(mongoDB)
    document_handler = DocumentHandler("ulpgc-inv-index\datalake\content")
    local_inverted_index = LocalInvertedIndex(inverted_index_handler, document_handler)

    start = time.time()
    local_inverted_index.insert_all_documents()
    end = time.time()

    print(f"Generating time: {end - start}")

    start = time.time()
    local_inverted_index.post_index()
    end = time.time()

    print(f"Posting time: {end - start}")"""