from planner import Planner
from tools import calculate, rag_search
import json


class Agent:

    def __init__(self, api_key):
        self.planner = Planner(api_key)
        self.tools = {
            "calculate": calculate,
            "rag_search": rag_search
        }

    def run(self, query):

        decision = self.planner.decide(query)

        print("Planner Decision:")
        print(decision)

        try:
            decision = json.loads(decision)
        except json.JSONDecodeError:
            return "Error: Invalid JSON response from planner."

        tool = decision["tool"]
        tool_input = decision["input"]

        if tool in self.tools:

            result = self.tools[tool](tool_input)

            answer = self.planner.respond(
                query,
                result
            )

            return answer

        elif tool == "none":
            
            answer = self.planner.respond(
                query
            )

            return answer
        
        else:
            return f"Unknown tool requested by planner: {tool}"
        
        
