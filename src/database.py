from llama_index.storage.docstore import MongoDocumentStore
from llama_index.storage.index_store import MongoIndexStore
from llama_index.storage.storage_context import StorageContext

def get_storage_context(uri, db_name):
    return StorageContext.from_defaults(
                docstore=MongoDocumentStore.from_uri(uri=uri, db_name=db_name),
                index_store=MongoIndexStore.from_uri(uri=uri, db_name=db_name),
            )
