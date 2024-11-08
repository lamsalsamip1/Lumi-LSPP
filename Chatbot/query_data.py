import argparse
# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def load_vector_store():
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def query_vector_store(db, query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0:
        print(f"Unable to find matching results.")
        
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    return context_text

def main():
    db = load_vector_store()
    model = OllamaLLM(model='llama3.2:1b', device='cuda')
    conversation_history = []

    while True:
        query_text = input("User: ")
        context_text = query_vector_store(db, query_text)
        if context_text is None:
            continue

        # Format the prompt with conversation history
        history_text = "\n".join([f"User: {q}\nLLaMA: {r}" for q, r in conversation_history])
        prompt = f"{history_text}\nUser: {query_text}\n{PROMPT_TEMPLATE.format(context=context_text, question=query_text)}"
        # print(prompt)

        response = model.invoke(prompt)
        print(f"\nLLaMA: {response}\n\n")

        # Record the conversation history
        conversation_history.append((query_text, response))

if __name__ == "__main__":
    main()