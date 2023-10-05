from os import listdir
import time

from indexer_sql.database_create import clean_database
from indexer_sql.SQLInvertedIndexHandler import SQLInvertedIndexHandler

creation_documents = listdir("datalake/content")[:10]
insertion_documents = listdir("datalake/content")[10:]

sqlinvertedindex = SQLInvertedIndexHandler()

def test_create_sql():
    global sqlinvertedindex
    durations = []

    for i in range(5):
        clean_database()
        print("Testing SQL with", 2*(i+1), "documents")
        start = time.time()
        sqlinvertedindex.inverted_index_of(creation_documents[:(2*(i+1))])
        end = time.time()
        print("Execution time (seconds):", end-start, "\n")
        durations.append(end-start)

    return durations

def test_insert_sql():
    global sqlinvertedindex
    durations = []
    step = 1
    cur = 0

    for i in range(5):
        print("Testing SQL with insert new ", cur+step, "documents")
        start = time.time()
        sqlinvertedindex.inverted_index_of(insertion_documents[cur:(cur+step)])
        end = time.time()
        print("Execution time (seconds):", end-start, "\n")
        durations.append(end-start)

        cur += step
        step += 1


    return durations



if __name__=='__main__':
    creation_durations = test_create_sql()
    insertion_duration = test_insert_sql()