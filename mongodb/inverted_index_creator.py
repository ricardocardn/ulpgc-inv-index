from os import listdir

class InvertedIndexCreator:
    """
    This class is responsible for creating the inverted index.
    """

    def __init__(self, mongoDB, inverted_index_handler):
        """Constructor of the class.
        :param mongoDB: MongoDB object
        :param inverted_index_handler: InvertedIndexHandler object
        """

        self.MongoDB = mongoDB
        self.inverted_index_handler = inverted_index_handler


    def insert_document(self, document_id):
        """Inserts the words of the document of id document in
        the inverted index.
        :param document_id: document id
        :return: inserted id
        """

        document = self.get_document(document_id)
        inserted_id = self.inverted_index_handler.insert_document(document, document_id)
        return inserted_id


    def insert_all_documents(self):
        """Inserts all documents in the inverted index.
        :return: True
        """

        documents = self.get_documents()
        for document in documents.keys():
            self.inverted_index_handler.insert_document(documents[document], document)
            

    def get_document(self, document_id):
        """Gets the document of id document_id.
        :param document_id: document id
        :return: document
        """

        with open(f"../datalake/content/{document_id}.txt", encoding="utf-8") as f:
            content_text = f.read()
        return content_text.split()
    

    def get_documents(self):
        """Gets all documents words.
        :return: documents
        """

        documents = listdir('datalake/content')
        documents_dict = dict()

        for document in documents:
            doc_name = document.replace(".txt", "")
            with open(f"datalake/content/{document}", encoding="utf-8") as f:
                documents_dict[int(doc_name)] = f.read().split()
        return documents_dict