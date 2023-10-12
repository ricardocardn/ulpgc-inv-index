import os
from .content_tokenizer import ContentTokenizer

class Indexer:

    def __init__(self, rute="datalake/content"):
        self.contentTokenizer = ContentTokenizer(rute)

    def insert_documents(self, documents = None, top = None):
        documents = self.contentTokenizer.get_documents(documents, top)

        for document_id, words in documents.items():
            self.insert_document(words, document_id)

    def insert_document(self, words, document_id):
        print(f"Inserting document {document_id}")
        for word in set(words):
            if not os.path.exists(f"datamart/{word}.txt"):
                with open(f"datamart/{word}.txt", "w") as f:
                    f.write(f"{document_id}" + ",")
            else:
                with open(f"datamart/{word}.txt", "a") as f:
                    f.write(f"{document_id}" + ",")

            
                

    
    
    