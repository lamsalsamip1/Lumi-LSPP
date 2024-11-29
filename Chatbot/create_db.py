from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import openai
import os
import shutil
from pathlib import Path
from langchain_openai import OpenAIEmbeddings

CHROMA_PATH = "chroma"
DATA_PATH = "data/courses/"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize lists to hold documents
md_documents = []

def main():
    generate_data_store() 


def generate_data_store():
    print("Start")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")
    chunks = split_text(documents)
    print("Chunks generated")
    save_to_chroma(chunks)


def load_documents():
    data_folder = Path(DATA_PATH)
    for file_path in data_folder.iterdir():
        if file_path.suffix == '.md':
            loader = UnstructuredMarkdownLoader(str(file_path))
            md_documents.extend(loader.load())
        # elif file_path.suffix == '.html':

    # Combine documents
    all_documents=md_documents
    return all_documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=300,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # document = chunks[10]
    # print(document.page_content)
    # print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # emb_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(model="text-embedding-3-small"), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()