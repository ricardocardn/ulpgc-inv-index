from os import listdir
import time

from indexer_nodb.indexer import Indexer
from indexer_nodb.indexer_manager import indexer_manager

creation_documents = listdir("datalake/content")[:10]
insertion_documents = listdir("datalake/content")[10:]
indexer = Indexer()

def test_create():
    durations = []
    global Indexer

    for i in range(5):
        indexer_manager.delete_directory()
        indexer_manager.create_directory()

        print("Testing with", 2*(i+1), "documents")
        time = measure_time(creation_documents[:2*(i+1)])
        print("Execution time (seconds):", time, "\n")

        durations.append(time)
        
    return durations

def test_insert():
    global indexer
    durations = []
    step = 1
    cur = 0

    for i in range(5):
        print("Testing with insert new ", step, "documents")
        time = measure_time(insertion_documents[cur:(cur+step)])
        print("Execution time (seconds):", time, "\n")
        durations.append(time)

        cur += step
        step += 1
    return durations

def measure_time(docs):
    global indexer


    start = time.time()
    indexer.insert_documents(docs, top=None)
    end = time.time()

    return end - start

if __name__=='__main__':
    creation_durations = test_create()
    insertion_duration = test_insert()