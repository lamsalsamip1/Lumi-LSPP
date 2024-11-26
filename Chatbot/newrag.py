from metaquery import get_metadata_content
from langchain_ollama.llms import OllamaLLM
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from openai import OpenAI
import os


CHROMA_PATH = "chroma"
openai.api_key = os.getenv("OPENAI_API_KEY")


## Initialize an empty list to store the conversation history
conversation_history = []


def load_vector_store():
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def query_vector_store(db, query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=6)
    if len(results) == 0 or results[0][1] < 0.3:
        print(f"Unable to find matching results.")
        
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    return context_text

def format_prompt(conversation_history, user_question,context_text, max_history=3):
    # Define the RAG prompt template with placeholders
    prompt_template = """
    You are Lumi, a knowledgeable assistant dedicated to answering questions related to courses and universities in Nepal. Answer the user's query based on the facts present in the retrieved context in a natural way. Access the chat history when needed. Like when user wants to compare two degrees, check the latest conversation history to find out what other course he is talking about. If you find no relevant information in the context, say that you don't know.

    ---

    **Conversation History:**
    {conversation_history}

    **Current User Question:** 
    {user_question}

    **Retrieved Context:**
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



# model = OllamaLLM(model='llama3.2:1b', device='cuda')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
last_context=None
db = load_vector_store()
# Main loop
while True:
    # Get user input
    user_question = input("You: ")
    
    # Assuming get_metadata_content is a function that takes the prompt and returns a response
    context_text = get_metadata_content(user_question)

    if not context_text:
        context_text = last_context if last_context else "I don't have any relevant context for this."
        print(context_text)
    
    if context_text=="RAG":
        print("performing rag to find out..")
        context_text = query_vector_store(db, user_question)
        

    # Replace the placeholder with the actual conversation history
    prompt = format_prompt(conversation_history, user_question, context_text)
    
    # Print the assistant's response
    model=ChatOpenAI(model="gpt-4o-mini")
    response=model.invoke(prompt)
   
    print(f"Lumi: {response.content}")
    conversation_history.append({"user": user_question, "assistant": response})
    last_context = context_text
    