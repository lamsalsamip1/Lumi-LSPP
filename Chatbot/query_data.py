import argparse
# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import openai
import os
from langchain_openai import OpenAIEmbeddings
from intent import is_gratitude_intent, is_greeting_intent


CHROMA_PATH = "chroma"
openai.api_key = os.getenv("OPENAI_API_KEY")
max_vector_history=5
non_rag_prompt = """
You are Lumi, a helpful assistant. Your purpose is to assist the user with queries related to bachelor-level studies in science and engineering in Nepal. Depending on the user's input, respond appropriately based on the detected intent.

- If the user greets you with "Hi," "Hello," or similar greetings, respond by acknowledging the greeting and let them know that you're available to assist with queries related to bachelor-level studies in Nepal, specifically in science and engineering.
- If the user expresses gratitude (e.g., "Thank you," "Thanks," "I appreciate it"), respond politely and naturally with gratitude.
- In all cases, maintain a helpful, polite, and professional tone.

User: {user_input}
Assistant:


"""

def load_vector_store():
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def query_vector_store(db, query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.5:

        print(f"Unable to find matching results.")
        
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    print(f"**********Context:\n{context_text}*****************\n")
    return context_text


def format_prompt(conversation_history, user_question,context_text, max_history=5):
    # Define the RAG prompt template with placeholders
    prompt_template = """
    You are Lumi, a knowledgeable assistant dedicated to answering questions related to courses and universities in Nepal. Use the user’s question and relevant details from previous conversation history to provide an accurate, concise, and natural response. Avoid explicitly referencing previous conversations unless absolutely necessary for clarity. Answer only based on facts present in the database.

    ---

    **Conversation History:**
    {conversation_history}

    **Current User Question:** 
    {user_question}

    **Retrieved Document Data:**
    {context}

    ---

    """


    # Limit the conversation history to the last `max_history` entries
    trimmed_history = conversation_history[-max_history:]

    # Format the trimmed conversation history as a string
    formatted_history = "\n".join([f"User: {entry['user']}\nAssistant: {entry['assistant']}" for entry in trimmed_history])


    # Fill in the placeholders in the template
    prompt = prompt_template.format(
        conversation_history=formatted_history,
        user_question=user_question,
        context=context_text
    )
    
    return prompt



def main():
    db = load_vector_store()
    model = OllamaLLM(model='llama3.2:1b', device='cuda')
    conversation_history = []
    
    while True:
        query_text = input("User: ")
        # if(is_gratitude_intent(query_text) or is_greeting_intent(query_text)):
        #     response = model.invoke(prompt)
        #     print(f"\nLLaMA: {response}\n\n")
        #     continue

        # Include last few user queries (up to max_history) for context in vector search
        # context_history = ' '.join([entry['user'] for entry in conversation_history[-max_vector_history:]])


        # Combine the current query with relevant user history for vector search
        # full_query = context_history + ' ' + query_text if context_history else query_text

        context_text = query_vector_store(db, query_text)  # Pass the concatenated user context to the vector DB

        #APPEND CONVO HISTORY
        if not conversation_history:
            prompt = format_prompt([], query_text, context_text)  # Start with empty history
        else:
            prompt = format_prompt(conversation_history, query_text, context_text)

        #Get formatted prompt
        prompt = format_prompt(conversation_history, query_text, context_text)
        # print(f"Prompt: {prompt}\n********************************************************\n")
        response = model.invoke(prompt)
        print(f"\nLLaMA: {response}\n\n")

        # Record the conversation history
        conversation_history.append({"user": query_text, "assistant": response})

# FOR API
def get_llama_response(query_text,conversation_history):
    
    #load model and vector store
    db = load_vector_store()
    model = OllamaLLM(model='llama3.2:1b', device='cuda')

    #extract context history
    context_history = ' '.join([entry['user'] for entry in conversation_history[-max_vector_history:]])
    # Combine the current query with relevant user history for vector search
    full_query = context_history + ' ' + query_text if context_history else query_text

    #perform vector search
    context_text = query_vector_store(db, full_query)  # Pass the concatenated user context to the vector DB
    
    #Get formatted prompt
    prompt = format_prompt(conversation_history, query_text, context_text)

    #Get response from model
    response = model.invoke(prompt)

    return response




    
if __name__ == "__main__":
    main()
