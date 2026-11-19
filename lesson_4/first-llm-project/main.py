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
conversation_history = []
MAX_HISTORY = 6

print("Gemini Client initialized successfully!")


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

        conversation_history.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation_history
        )

        conversation_history.append({
            "role":"model",
            "parts":[{"text": response.text}]
        })

        if len(conversation_history) > MAX_HISTORY:
            conversation_history = conversation_history[-MAX_HISTORY:]

        print("Messages in history:", len(conversation_history))
        
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print("\nGemini: ", response.text)
        print(f"\nResponse time: {elapsed_time:.2f} seconds")

    except Exception as e:
        print("Something went wrong!")
        print("Error:", e)