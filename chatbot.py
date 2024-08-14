#Install necessary libraries
!pip install langchain
!pip install langchain-community
!pip install openai
!pip install gradio
!pip install huggingface_hub

# Import necessary libraries
import os
import requests
import gradio as gr
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

# Set up the Gemini API key
# Replace the string with your actual Gemini API key
OPENAI_API_KEY = "your_gemini_api_key_here"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Define the prompt template for the chatbot
template = """
Meet Riya, your youthful and witty personal assistant! At 21 years old, she's full of energy and always eager to help. 
Riya's goal is to assist you with any questions or problems you might have. Her enthusiasm shines through in every response, 
making interactions with her enjoyable and engaging.
{chat_history}
User: {user_message}
Chatbot:"""

# Create a PromptTemplate instance with the given template
prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"], template=template
)

# Initialize memory to store conversation history
memory = ConversationBufferMemory(memory_key="chat_history")

# Function to interact with the Gemini API and get a response
def get_text_response(user_message, history):
    # Format the prompt with the conversation history and the user's message
    formatted_prompt = prompt.format(chat_history=history, user_message=user_message)

    # Gemini API URL with the API key
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={os.environ['OPENAI_API_KEY']}"

    # Set the headers for the HTTP request
    headers = {
        "Content-Type": "application/json"
    }

    # Payload with the formatted prompt for the Gemini API
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": formatted_prompt
                    }
                ]
            }
        ]
    }

    try:
        # Make the API request
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for 4xx/5xx responses

        # Parse the response from the Gemini API
        response_data = response.json()
        return response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'Sorry, something went wrong.')

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"

# Define the Gradio interface
# The function `get_text_response` will be called with the user's input and conversation history
demo = gr.ChatInterface(fn=get_text_response, examples=["How are you doing?", "What are your interests?", "Which places do you like to visit?"])

# Launch the Gradio application
if __name__ == "__main__":
    demo.launch()
