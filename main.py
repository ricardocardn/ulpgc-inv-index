from datalake_builder import create_datalake

from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

mongoDB = MongoDB()
indexer = Indexer(mongoDB)

if __name__ == '__main__':
    create_datalake()
    # indexer.insert_all_documents()

    inv_index = indexer.get_index()
    print(inv_index)