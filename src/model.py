from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import ServiceContext


def get_service_context(model_name):
    embed_model = HuggingFaceEmbeddings(
    model_name=model_name
)
    service_context = ServiceContext.from_defaults(embed_model=embed_model)
    return service_context
