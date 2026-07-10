from agent import Agent
import os
from dotenv import load_dotenv

load_dotenv()

agent = Agent(os.getenv("GROQ_API_KEY"))


while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = agent.run(query)

    print("Agent:", response)
    
