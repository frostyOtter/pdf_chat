import requests
from pathlib import Path
from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
# from llama_index.response.notebook_utils import display_response
from IPython.display import display, Markdown
from typing import Optional, Sequence
from llama_index.schema import Document
from llama_index import VectorStoreIndex


def read_pdf_from_link(pdf_path:str, local_path:str)-> Optional[Sequence[Document]]:
    # Init pdf reading tool
    PDFReader = download_loader("PDFReader")
    loader = PDFReader()
    # if link given is web-base
    if pdf_path.startswith("https"):
        r = requests.get(pdf_path)
        # download and write to localfile
        with open(local_path, 'wb') as f:
            f.write(r.content)
        
        # Load to corpus text
        doc = loader.load_data(file=Path(local_path))[0]
    # if link given is local
    # Load to corpus text
    else: doc = loader.load_data(file=Path(pdf_path))[0]
    
    # parse corpus to nodes
    nodes = SimpleNodeParser().get_nodes_from_documents([doc])

    return nodes

def print_menu():
    print("#"*5)
    print("1. Enter question")
    print("2. Exit")

def get_response(user_query:str, vector_index:VectorStoreIndex)->str:
    # Get response from llama_index api
    vector_response = vector_index.as_query_engine().query(user_query) 
    # Display response
    display(Markdown(f"<b>{vector_response}</b>"))