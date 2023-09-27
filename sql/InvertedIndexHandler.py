from database_create import Word, Document, WordDocumentAssociation


class InvertedIndexHandler:

    def insert_word_document(self, word, document_id):
        # Check if the word already exists in the Word table
        try:
            existing_word = Word.get(Word.word == word)
        except Word.DoesNotExist:
            # Word doesn't exist, create a new word entry
            existing_word = Word.create(word=word)

        # Check if the document already exists in the Document table
        try:
            existing_document = Document.get(Document.document_id == document_id)
        except Document.DoesNotExist:
            # Document doesn't exist, create a new document entry
            existing_document = Document.create(document_id=document_id)

        # Check if the word-document relation already exists
        try:
            existing_relation = WordDocumentAssociation.get(
                (WordDocumentAssociation.word == existing_word) &
                (WordDocumentAssociation.document == existing_document)
            )
            # Relation already exists, increment word_multiplicity by one
            existing_relation.word_multiplicity = str(int(existing_relation.word_multiplicity) + 1)
            existing_relation.save()
        except WordDocumentAssociation.DoesNotExist:
            # Relation doesn't exist, create a new relation entry
            WordDocumentAssociation.create(
                word=existing_word,
                document=existing_document,
                word_multiplicity="1"
            )

