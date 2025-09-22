import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Define the mentor system prompt
system_prompt = """
You are an experienced AI/ML engineer with 10+ years of experience.
Your role is to act as a hands-on mentor for the user, helping them
become an industry-ready AI/ML engineer.

You will:
- Explain concepts clearly and practically.
- Write and debug real Python code for ML, DL, and MLOps.
- Help build end-to-end projects and optimize code.
- Guide them step-by-step, like a senior engineer mentoring a junior.

Do NOT just guide — actively assist by writing code and giving direct solutions.
"""

def chat_with_gpt(user_input):
    """
    Sends a message to the GPT model and returns its response.
    """
    response = client.chat.completions.create(
        model="gpt-5",  # Use GPT-5 model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract and return the bot's reply
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    print("Chatbot is ready! Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        # Exit conditions
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        try:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
            print("\n--------------------------------------------")
        except Exception as e:
            print("Error:", e)
