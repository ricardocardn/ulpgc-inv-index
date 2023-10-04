from datalake_builder import create_datalake

from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB
from indexer_nosql.document_handler import DocumentHandler

mongoDB = MongoDB()
document_handler = DocumentHandler("datalake/content")
indexer = Indexer(mongoDB, document_handler)

def mongo_inverted_index():
    global mongoDB

    cursor = mongoDB.col.find({})
    inverted_index = dict()
    
    for word in cursor:
        inverted_index[word["word"]] = word["documents"]

    return inverted_index
    

if __name__ == '__main__':
    # create_datalake()
    # indexer.insert_all_documents()

    inv_index = mongo_inverted_index()
    print(inv_index)