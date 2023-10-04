from os import listdir

class DocumentHandler:
    def __init__(self, rute):
        self.rute = rute
    
    def get_documents(self):
        documents = listdir(self.rute)
        documents_dict = dict()

        for document in documents:
            doc_name = document.replace(".txt", "")
            documents_dict[int(doc_name)] = self.get_document(doc_name)

        return documents_dict
    
    def get_document(self, document_id):
        with open(f"{self.rute}\{document_id}.txt", encoding="utf-8") as f:
            content_text = f.read()
        return content_text.split()