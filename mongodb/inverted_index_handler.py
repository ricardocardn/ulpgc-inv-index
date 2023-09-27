import pymongo

class InvertedIndexHandler:
    """
    This class is responsible for handling the inverted index.
    """

    def __init__(self, MongoDB):
        """Constructor of the class.
        :param MongoDB: MongoDB object
        """

        self.MongoDB = MongoDB

    def insert_document(self, words, document_id):
        """Inserts the words of the document of id document in
        the inverted index.
        :param document_id: document id
        :return: inserted id
        """

        for position, word in enumerate(words):
            self.insert_word_document(word, document_id, position)

        return True
        
    def insert_word_document(self, word, document_id, position):
        """Inserts the word of the document of id document_id in
        the inverted index.
        :param word: word
        :param document_id: document id
        :param position: position of the word in the document
        :return: inserted id
        """

        inserted_doc_id = self.MongoDB.add_word({
            "word": word,
            "documents": [document_id]
        })

        return inserted_doc_id
    

    def post_from_local(self, dict):
        for word in dict.keys():
            self.MongoDB.add_word({
                "word": word,
                "documents": list(dict[word])
            })