from planner import Planner
import os
from dotenv import load_dotenv

load_dotenv()

planner = Planner(os.getenv("GROQ_API_KEY"))

print(planner.decide("What is 25 * 18?"))
print()
print(planner.decide("Who invented Python?"))
