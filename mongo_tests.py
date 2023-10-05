from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

import time

mongoDB = MongoDB()
indexer = Indexer(mongoDB)
max_words_per_document = 2000

creation_documents = [['1519', '1524'],
                      ['1519', '1524', '24873', '2735'],
                      ['1519', '1524', '24873', '2735', '45', '5341'],
                      ['1519', '1524', '24873', '2735', '45', '5341', '5342', '57342'],
                      ['1519', '1524', '24873', '2735', '45', '5341', '5342', '57342', '71374', '71673']]

insertion_documents = [['71674', '71776'],
                       ['71674', '71776', '71777', '71783'],
                       ['71674', '71776', '71777', '71783', '71784', '71799'],
                       ['71674', '71776', '71777', '71783', '71784', '71799', '71802', '71803'],
                       ['71674', '71776', '71777', '71783', '71784', '71799', '71802', '71803', '71804', '71807']]
    

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
        print("Testing mongoDB with documents", creation_documents[i],"(empty db)")
        return test_mongo_file(creation_documents[i])
    else:
        global insertion_documents
        print("Testing mongoDB with documents", insertion_documents[i],"(non empty db)")
        for doc in insertion_documents[i]:
            mongoDB.delete_document(int(doc))

        return test_mongo_file(insertion_documents[i])


def test_mongo(empty = False):
    global mongoDB
    if empty:
        mongoDB.clean_db()

    durations = []

    for i in range(5):
        duration = test_mongo_several_files(i, empty)
        print("Execution time (seconds):", duration, "\n")
        durations.append(duration)

    return durations


if __name__ == '__main__':
    test_mongo(empty=True)
    test_mongo()