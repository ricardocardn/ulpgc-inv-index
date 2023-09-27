from os import listdir

class InvertedIndexCreator:
    def __init__(self, mongoDB, inverted_index_handler):
        self.MongoDB = mongoDB
        self.inverted_index_handler = inverted_index_handler


    def insert_document(self, document_id):
        document = self.get_document(document_id)
        inserted_id = self.inverted_index_handler.insert_document(document, document_id)
        return inserted_id


    def insert_all_documents(self):
        documents = self.get_documents()
        for document in documents.keys():
            self.inverted_index_handler.insert_document(documents[document], document)

        return True
            

    def get_document(self, document_id):
        with open(f"../datalake/content/{document_id}.txt", encoding="utf-8") as f:
            content_text = f.read()

        return content_text.split()
    

    def get_documents(self):
        documents = listdir('datalake/content')
        documents_dict = dict()

        for document in documents:
            doc_name = document.replace(".txt", "")
            with open(f"datalake/content/{document}", encoding="utf-8") as f:
                documents_dict[int(doc_name)] = f.read().split()

        return documents_dict
    

if __name__ == '__main__':
    print("Inverted Index Creator")