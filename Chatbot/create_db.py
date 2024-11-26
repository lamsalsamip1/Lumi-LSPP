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

# Metadata mapping for demonstration (assign dynamically based on your logic)
METADATA_MAP = {
    "bca.md": {"courses": ["BCA","Bachelor in Computer Application","Computer Application"], "university": ["Tribhuvan University", "TU"]},

    "bim.md": {"courses": ["BIM","Bachelor in Information Management","Information Management"], "university": ["Tribhuvan University", "TU"]},

    "csit.md": {"courses": ["CSIT","BSc.CSIT","Bachelor in Computer Science and Information Technology","Computer Science and Information Technology"], "university": ["Tribhuvan University", "TU"]},

    "bit.md": {"courses": ["BIT","Bachelor in Information Technology","Information Technology","Bachelor in IT"], "university": ["Tribhuvan University", "TU"]},

    "cs-ku.md": {"courses": ["BSc.CS","Bachelor in Computer Science","Computer Science"], "university": ["Kathmandu University", "KU"]},

    "btechAI.md": {"courses": ["B.Tech AI","btech AI","Bachelor in Artificial Intelligence","Artificial Intelligence","Bachelor of Technology in AI"], "university": ["Kathmandu University", "KU"]},

    "bce-tu.md": {"courses": ["BCE","Bachelor in Civil Engineering","Civil Engineering","BE Civil","Civil Eng","Civil"], "university": ["Tribhuvan University", "TU"]},

    "ce-ku.md": {"courses": ["BE Civil","Bachelor in Civil Engineering","Civil Engineering","Civil Eng","Civil"], "university": ["Kathmandu University", "KU"]},

    # "be-electrical.md": {"courses": ["BE Electrical","Bachelor in Electrical Engineering","Electrical Engineering","Electrical Eng"], "university": ["Kathmandu University", "KU"]},
    "be-aero-tu.md": {"courses": ["BE Aerospace","Bachelor in Aerospace Engineering","Aerospace Engineering","Aerospace Eng","Aerospace"], "university": ["Tribhuvan University", "TU"]},

    "be-agriculture-tu.md": {"courses": ["BE Agriculture","Bachelor in Agriculture Engineering","Agriculture Engineering","Agriculture Eng"], "university": ["Tribhuvan University", "TU"]},

    "be-automobile-tu.md": {"courses": ["BE Automobile","Bachelor in Automobile Engineering","Automobile Engineering","Automobile Eng"], "university": ["Tribhuvan University", "TU"]},
    
    "be-elect-ku.md": {"courses": ["BE Electrical and Electronics","Bachelor in Electrical and Electronics Engineering","Electrical and Electronics Engineering","Electrical Eng","Electrical Engineering","Electronics Engineering","Electronics Eng","Electronics and Electrical"], "university": ["Kathmandu University", "KU"]},

    "be-geomatics-ku.md": {"courses": ["BE Geomatics","Bachelor in Geomatics Engineering","Geomatics Engineering","Geomatics Eng","Geomatics"], "university": ["Kathmandu University", "KU"]},

    "be-industrial-tu.md": {"courses": ["BE Industrial","Bachelor in Industrial Engineering","Industrial Engineering","Industrial Eng","Industrial"], "university": ["Tribhuvan University", "TU"]},

    "be-mechanical-tu.md": {"courses": ["BE Mechanical","Bachelor in Mechanical Engineering","Mechanical Engineering","Mechanical Eng","Mechanical"], "university": ["Tribhuvan University", "TU"]},

    "be-elect-TU.md": {"courses": ["BE Electronics Information and Communication","Bachelor in Electronics Engineering","Bachelor of Electronics, Communication and Information Engineering","Electronics, Information and Communication Engineering","Electronics Eng","Information Eng","Communication Eng","Electronics Information and Communication"], "university": ["Tribhuvan University", "TU"]},

    "bel-tu.md":{"courses":["BE Electrical","Bachelor in Electrical Engineering","Electrical Engineering","Electrical Eng"], "university": ["Tribhuvan University", "TU"]},

    "bit-herald.md": {"courses": ["BIT","Bachelor in Information Technology","Information Technology","Bachelor in IT","bsc hons","hons"], "university": ["Herald College", "Herald","University of Wolverhampton","Herald College Kathmandu","foreign university"]},

    "bsc-comp-islington.md": {"courses": ["BSc Computing","Bachelor in Computing","Computing","bsc hons","hons"], "university": ["Islington College", "Islington","London Metropolitan University","London Met University","foreign university"]},

    "CE_TU.md":{"courses":["BE Computer","Bachelor in Computer Engineering","Computer Engineering","Computer Eng","Comp Eng","Comp Engineering","Bachelor of Engineering in Computer Engineering"], "university": ["Tribhuvan University", "TU"]},

    "CE-KU.md":{"courses":["BE Computer","Bachelor in Computer Engineering","Computer Engineering","Computer Eng","Comp Eng","Comp Engineering","Bachelor of Engineering in Computer Engineering"], "university": ["Kathmandu University", "KU"]},

    "se-pu.md": {"courses": ["Software Engineering","Bachelor in Software Engineering","Software Eng","Software","Bachelor in Software","Bachelor of Engineering in Software Engineering"], "university": ["Pokhara University", "PU"]},

    "be-chemical-tu.md": {"courses": ["BE Chemical","Bachelor in Chemical Engineering","Chemical Engineering","Chemical Eng","Bachelor of Engineering in Chemical Engineering"], "university": ["Tribhuvan University", "TU"]},





}


def main():
    print(len(METADATA_MAP))
    generate_data_store()
    
def flatten_metadata(metadata):
    """
    Converts lists in metadata to comma-separated strings.
    """
    return {key: ", ".join(value) if isinstance(value, list) else value for key, value in metadata.items()}

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
            # md_documents.extend(loader.load())
            mds=loader.load()
            combined_content = "\n\n".join(doc.page_content for doc in mds)
            metadata = METADATA_MAP.get(file_path.name, {})  # Get metadata dynamically
            doc = Document(page_content=combined_content, metadata=metadata)  # Create one Document
            md_documents.append(doc) 

    # Combine documents
    all_documents = md_documents
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

     # Flatten metadata for each document
    for chunk in chunks:
        chunk.metadata = flatten_metadata(chunk.metadata)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(model="text-embedding-3-small"), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()