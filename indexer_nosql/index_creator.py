from mongo_db_manager import MongoDB
from indexer import Indexer

def main():
    mongoDB = MongoDB()
    indexer = Indexer(mongoDB, "datalake/content")

    indexer.insert_all_documents()


if __name__ == "__main__":
    main()