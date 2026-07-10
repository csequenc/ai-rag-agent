import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # Load environment variables from .env file

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1
)

response = llm.invoke("What is AI in 10 words?")

print(type(response))
print(response.response_metadata)
