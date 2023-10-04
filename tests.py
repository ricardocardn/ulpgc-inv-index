from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB
from indexer_nosql.document_handler import DocumentHandler

import time

mongoDB = MongoDB()
document_handler = DocumentHandler("datalake/content")
indexer = Indexer(mongoDB, document_handler)

document_ids = ['45', '2735', '5341', '5342', '24873', '71673']

def insert_documents(docs):
    global indexer
    indexer.insert_documents(docs)


def test_mongo_n_files(n):
    start = time.time()
    insert_documents(document_ids[:2:n])
    end = time.time()

    duration = end - start
    print(f"Time for {n} documents: {duration} seconds")
    return duration


def test_mongo():
    mongoDB.col.delete_many({})
    mongoDB.documents_col.delete_many({})

    durations = []
    global document_ids

    for i in range(1, 7):
        durations.append(test_mongo_n_files(i))

    return durations


if __name__ == '__main__':
    test_mongo()