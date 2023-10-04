from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

import time

mongoDB = MongoDB()
indexer = Indexer(mongoDB)

creation_documents = [['45', '2735'],
                      ['45', '2735', '5341', '5342'],
                      ['45', '2735', '5341', '5342', '24873', '71673']]

insertion_documents = [['71674', '71776'], 
                       ['71777', '71783', '71784']]


def clean_mongo_db():
    global mongoDB
    mongoDB.col.delete_many({})
    mongoDB.documents_col.delete_many({})
    

def insert_to_mongo(docs):
    global indexer

    start = time.time()
    indexer.insert_documents(docs)
    end = time.time()

    return end - start


def test_mongo_files(i, empty):
    if empty:
        global creation_documents
        print("Testing mongoDB with documents", creation_documents[i],"(empty db)")
        return insert_to_mongo(creation_documents[i])
    else:
        global insertion_documents
        print("Testing mongoDB with documents", insertion_documents[i],"(not empty db)")
        return insert_to_mongo(insertion_documents[i])


def test_mongo(empty = False):
    if empty:
        clean_mongo_db()

    durations = []

    for i in range(5):
        duration = test_mongo_files(i, empty)
        print("Execution time (seconds):", duration, "\n")
        durations.append(duration)

    return durations


if __name__ == '__main__':
    test_mongo(empty=True)
    test_mongo()