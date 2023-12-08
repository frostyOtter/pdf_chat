# Chatting with your PDF/Document (WIP)
    - Project in still work in progress, 
    - Reference from llama-index docs
    
## Config: 
    - Database: MongoDB
    - Embedding Service: sentence-transformers
    - Framework: llama-index, langchain

## .env
    - DATABASE_URI: 'your-mongodb-uri'
    - DATABASE_NAME: 'your-mongodb-database-name'

### run command:

    python main.py\
            --model \ 
            --local_path \ 


### default values:
    - model: "default: str "sentence-transformers/all-mpnet-base-v2" "
    - local_path: "default: str "/content/paper.pdf" "