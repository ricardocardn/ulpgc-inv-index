from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

import time
from os import listdir

mongoDB = MongoDB()
indexer = Indexer(mongoDB)
max_words_per_document = 2000

creation_documents = listdir("datalake/content")[:10]
insertion_documents = listdir("datalake/content")[10:]
    

def test_mongo_files(docs):
    global indexer
    global max_words_per_document

    print("Inserting documents", docs, "into MongoDB")

    start = time.time()
    indexer.insert_documents(docs, top=max_words_per_document)
    end = time.time()

    return end - start


def test_mongo_create():
    global mongoDB

    durations = []
    for i in range(5):
        mongoDB.clean_db()
        duration = test_mongo_files(creation_documents[:2*(i+1)])

        print("Execution time (seconds):", duration, "\n")
        durations.append(duration)

    return durations


def test_mongo_insert():
    durations = []
    step = 1
    cur = 0

    for i in range(5):
        duration = test_mongo_files(insertion_documents[cur:(cur+step)])

        print("Execution time (seconds):", duration, "\n")
        durations.append(duration)

        cur += step
        step += 1

    return durations


if __name__ == '__main__':
    creation_durations = test_mongo_create()
    insertion_duration = test_mongo_insert()

    print("Creation values:", creation_durations)
    print("Average creation time (seconds):", sum(creation_durations) / len(creation_durations))

    print("Insertion values:", insertion_duration)
    print("Average insertion time (seconds):", sum(insertion_duration) / len(insertion_duration))