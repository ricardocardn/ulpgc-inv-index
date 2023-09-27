class LocalInvertedIndex:
    def __init__(self, inverted_index_handler, document_handler):
        self.inverted_index = inverted_index_handler
        self.doc = document_handler
        self.dict = dict()

    def insert_all_documents(self):
        documents = self.doc.get_documents()
        for document in documents.keys():
            self.insert_words(documents[document], document)


    def insert_document(self, document_id):
        document = self.doc.get_document(document_id)
        self.insert_words(document, document_id)


    def insert_words(self, words, document_id):
        for position, word in enumerate(words):
            self.insert_word(word, document_id, position)


    def insert_word(self, word, document_id, position):
        if word not in self.dict:
            try:
                self.dict[word] = set()

            except:
                #self.post_index()
                #self.insert_word(word, document_id, position)
                pass

        self.dict[word].add(document_id)

    def post_index(self):
        self.inverted_index.post_from_local(self.dict)
        self.dict = dict()


if __name__ == '__main__':
    local_inverted_index = LocalInvertedIndex(None)
    local_inverted_index.insert_all_documents()

    print(local_inverted_index.dict)

    for word in local_inverted_index.dict.keys():
        if len(local_inverted_index.dict[word]) > 1:
            print(word, local_inverted_index.dict[word])