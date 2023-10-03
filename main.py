from datalake_builder import create_datalake
from indexer_nosql.index_creator import index_creator


if __name__ == '__main__':
    create_datalake()
    inverted_index = index_creator()
    print(inverted_index)


def time_measures():
    # measure of databaste 
    #measure od no sql
    pass