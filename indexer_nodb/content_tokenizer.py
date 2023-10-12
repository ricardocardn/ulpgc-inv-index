from os import listdir

class ContentTokenizer:
    def __init__(self, rute):
        self.rute = rute
    

    def get_documents(self, docs = None, top = None):
        documents = self.get_ids(docs)
        
        
        documents_dict = dict()
        for document in documents:
            doc_name = document.replace(".txt", "")
            documents_dict[int(document)] = self.get_document(document)[:top]

        return documents_dict


    def get_document(self, document_id):
        with open(f"{self.rute}\{document_id}.txt", encoding="utf-8") as f:
            content_text = f.read()
        return content_text.split()
    

    def get_ids(self, docs = None):
        documents = docs if docs else listdir(self.rute)
        documents = [document.replace(".txt", "") for document in documents]
        return documents