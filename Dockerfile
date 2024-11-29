# Use a Python base image from Docker Hub
FROM python:3.10-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY Chatbot/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY Chatbot/ /app/

# Expose the port the app will run on
EXPOSE 8000

# Set the entrypoint for the container to run the create_db.py script and then Gunicorn
CMD ["sh", "-c", "python create_db.py && python app.py"]