import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini key not found!")

client = genai.Client(api_key=api_key)

print("Gemini client initialized successfully")

# prompt = input("Enter prompt: ").strip()

# # List models available to your API key
# for model in client.models.list():
#     print(model.name)

# conversation = []

# if prompt:
#     try:
#         conversation.append({
#             "role": "user",
#             "content":prompt
#         })
#         response = client.models.generate_content(
#             model="gemini-3.5-flash",
#             contents=prompt
#         )

#         conversation.append({
#             "role": "assistant",
#             "content":response.text
#         })

#         print("\nGemini's Response:")
#         print(response.text)
#     except Exception as e:
#         print("Something went wrong!!")
#         print("Error:", e)
# else:
#     print("Please enter a prompt!")


chat = client.chats.create(
    model = "gemini-3.5-flash"
)

while True:
    prompt = input("\nYou: ").strip()

    if prompt.lower() == "exit":
        print("Chat ended!")
        break

    if not prompt:
        print("Please enter a prompt!")
        continue

    try:
        response = chat.send_message(prompt)
        print("\nGemini:", response.text)

    except Exception as e:
        print("Something went wrong!!")
        print("Error:", e)

