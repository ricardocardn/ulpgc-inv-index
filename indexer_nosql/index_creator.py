from mongo_db_manager import MongoDB
from inverted_index_handler import InvertedIndexHandler
from local_inverted_index import LocalInvertedIndex
from document_handler import DocumentHandler
import time


class Indexer:

    def __init__(self, mongoDB):
        self.inverted_index_handler = InvertedIndexHandler(mongoDB)
        self.document_handler = DocumentHandler("ulpgc-inv-index\datalake\content")
        self.index = LocalInvertedIndex(self.inverted_index_handler, self.document_handler)


def indexer(document_list):
    indexer = Indexer(MongoDB())
    indexer.index.insert_all_documents()