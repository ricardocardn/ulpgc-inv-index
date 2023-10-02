from mongo_db_manager import MongoDB
from inverted_index_handler import InvertedIndexHandler
from local_inverted_index import LocalInvertedIndex
from document_handler import DocumentHandler
import time

def index_creator():
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

    print(f"Posting time: {end - start}")

    return local_inverted_index.dict