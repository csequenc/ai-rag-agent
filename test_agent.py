from agent import Agent
import os
from dotenv import load_dotenv

load_dotenv()

agent = Agent(os.getenv("GROQ_API_KEY"))

print(agent.run("What is 15 * 27?"))
print(agent.run("Who invented Python?"))
