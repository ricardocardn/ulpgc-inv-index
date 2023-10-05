from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

database = SqliteDatabase('inverted-index-db.db')


class BaseModel(Model):
    class Meta:
        database = database


class Word(BaseModel):
    word = CharField(unique=True)


class Document(BaseModel):
    document_id = CharField(primary_key=True)


class WordDocumentAssociation(BaseModel):
    word = ForeignKeyField(Word, backref='documents')
    document = ForeignKeyField(Document, backref='words')
    word_multiplicity = CharField()


database.connect()
database.create_tables([Word, Document, WordDocumentAssociation])

def delete_tables():
    database.drop_tables([Word, Document, WordDocumentAssociation])

