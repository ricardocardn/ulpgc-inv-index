from os import listdir

class DocumentHandler:
    def __init__(self, rute):
        self.rute = rute


    def get_document(self, document_id):
        """Gets the document of id document_id.
        :param document_id: document id
        :return: document
        """

        with open(f"ulpgc-inv-index\datalake\content\{document_id}.txt", encoding="utf-8") as f:
            content_text = f.read()
        return content_text.split()
    

    def get_documents(self):
        """Gets all documents words.
        :return: documents
        """

        documents = listdir('ulpgc-inv-index\datalake\content')
        documents_dict = dict()

        for document in documents:
            doc_name = document.replace(".txt", "")
            with open(f"ulpgc-inv-index\datalake\content\{document}", encoding="utf-8") as f:
                documents_dict[int(doc_name)] = f.read().split()
        return documents_dict