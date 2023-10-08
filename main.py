from datalake_builder import create_datalake

from indexer_nosql.indexer import Indexer
from indexer_nosql.mongo_db_manager import MongoDB

from os import listdir as listdir

mongoDB = MongoDB()
indexer = Indexer(mongoDB)

def inverted_index_of(document_list)->(dict):
    global indexer
    global mongoDB

    indexer.insert_documents(document_list)
    return mongoDB.get_index_of(
            [int(i.replace(".txt", "")) for i in document_list]
        )


if __name__ == '__main__':
    create_datalake()
    inverted_index = inverted_index_of(listdir("datalake/content")[:3])
    
    print(inverted_index)