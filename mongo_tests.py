from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

import time

mongoDB = MongoDB()
indexer = Indexer(mongoDB)
max_words_per_document = 2000

creation_documents = ['1519', '1524', '24873', '2735', '45', '5341', '5342', '57342', '71374', '71673'] 
insertion_documents = ['71674', '71776', '71777', '71783', '71784', '71799', '71802', '71803', '71804', '71807']
    

def test_mongo_file(docs):
    global indexer
    global max_words_per_document

    start = time.time()
    indexer.insert_documents(docs, top=max_words_per_document)
    end = time.time()

    return end - start


def test_mongo_several_files(i, empty):
    global mongoDB
    if empty:
        global creation_documents
        print("Testing mongoDB with documents", creation_documents[:i],"(empty db)")
        return test_mongo_file(creation_documents[:i])
    else:
        global insertion_documents
        print("Testing mongoDB with documents", insertion_documents[:i],"(non empty db)")
        for doc in insertion_documents[:i]:
            mongoDB.delete_document(int(doc))

        return test_mongo_file(insertion_documents[:i])


def test_mongo(empty = False):
    global mongoDB

    durations = []
    for i in range(5):
        if empty: 
            mongoDB.clean_db()

        duration = test_mongo_several_files(2*(i+1), empty)
        print("Execution time (seconds):", duration, "\n")
        durations.append(duration)

    return durations


if __name__ == '__main__':
    creation_durations = test_mongo(empty=True)
    insertion_duration = test_mongo()

    print("Creation values:", creation_durations)
    print("Average creation time (seconds):", sum(creation_durations) / len(creation_durations))

    print("Insertion values:", insertion_duration)
    print("Average insertion time (seconds):", sum(insertion_duration) / len(insertion_duration))