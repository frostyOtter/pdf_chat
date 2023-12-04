from database import storage_context
from utils import read_pdf_from_link, print_menu, get_response
from model import get_service_context

import os
import argparse
from llama_index import VectorStoreIndex
from dotenv import load_dotenv
load_dotenv()


def config():
    parser = argparse.ArgumentParser(description='Run this file to chat with your pdf file')
    parser.add_argument('--model', type=str, default="sentence-transformers/all-mpnet-base-v2",
                                    help='path to huggingface model')
    parser.add_argument('--local_path', type=str, default="/content/paper.pdf",
                                    help='path to your pdf')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # Init input args
    args = config()
    # Paste pdf link
    link_to_pdf = input("Paste your link to pdf file: ")
    # Read pdf file from given link
    nodes = read_pdf_from_link(pdf_path = link_to_pdf, local_path=args.local_path)
    # Init data
    storage = storage_context(uri=os.environ['DATABASE_URI'], db_name=os.environ['DATABASE_NAME'])
    # Init model
    service_context = get_service_context(args.model)

    # Paste data through model into embedding vectors
    vector_index = VectorStoreIndex(documents = nodes,
                                    storage_context = storage,
                                    service_context = service_context,
                                    show_progress = True)

    print("Database loaded")
    print("Chat ready...")
    print("Start asking your bot...")
    while True:
        print_menu()
        user_query = input("Enter query: ")
        get_response(user_query = user_query, vector_index=vector_index)

