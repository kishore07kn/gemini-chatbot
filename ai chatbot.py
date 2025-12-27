
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

myapi_key=os.getenv("YOUR_GEMINI_API_KEY")
genai.configure(api_key=myapi_key)


model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

print("Gemini Bot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Gemini Bot: Goodbye 👋")
        break

    response = model.generate_content(user)
    print("Gemini Bot:", response.text)
