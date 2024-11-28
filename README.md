## Lumi-LSPP

# Steps to Run the Chatbot API

Step 1: Clone the repository

Step 2: Go to the Chatbot Folder
`cd chatbot`

Step 3: Install the requirements
`pip install -r requirements.txt`

Step 4: Recreate the chroma database
`python create_db.py`

Step 5: Add your Open AI API Key to your environment variable OPENAI_API_KEY

Step 5: Run the flask app
`python app.py`
