import os
from dotenv import load_dotenv
from google import genai
import time

# Load environment variables
load_dotenv()

# Retreive API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini key not found!")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

print("Gemini Client initialized successfully!")

# Create a chat session
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

print("\nChat started! Type 'exit' to quit.")

while True:
    prompt = input("\nYou: ").strip()

    if prompt.lower() == "exit":
        print("Chat ended!")
        break

    if not prompt:
        print("Please enter a prompt!")
        continue

    try:
        start_time = time.perf_counter()
        response = chat.send_message(prompt)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print("\nGemini: ", response.text)
        print(f"\nResponse time: {elapsed_time:.2f} seconds")

    except Exception as e:
        print("Something went wrong!")
        print("Error:", e)