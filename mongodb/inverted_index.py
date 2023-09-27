import pymongo

class InvertedIndexHandler:
    def __init__(self, MongoDB):
        self.MongoDB = MongoDB

    def insert_document(self, words, document_id):
        for position, word in enumerate(words):
            self.insert_word_document(word, document_id, position)

        return True
        
    def insert_word_document(self, word, document_id, position):
        inserted_doc_id = self.MongoDB.add_word({
            "word": word,
            "documents": [
                {
                    "document_id": document_id,
                    "positions": [position]
                }
            ]
        })

        return inserted_doc_id