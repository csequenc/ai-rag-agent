from groq import Groq


class Planner:

    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def decide(self, query):

        prompt = f"""
        You are an AI agent.

        Available tools:

        1. calculate(expression)
        Use ONLY for mathematical calculations.

        2. rag_search(question)
        Use when the answer is likely contained in the uploaded documents.

        3. none
        Use when neither tool is needed.

        Return ONLY valid JSON.

        If a tool is needed:

        {{
            "tool": "calculate",
            "input": "<expression>"
        }}
        
        {{
            "tool": "rag_search",
            "input": "<user question>"
        }}

        Otherwise:

        {{
            "tool": "none",
            "input": ""
        }}

        User:
        {query}
        """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    def respond(self, query, observation = None):
        
        if observation is None:
            prompt = f"""
    User asked:
    {query}
    
    No tool was used.
    
    Write the final answer for the user directly.
    """
        else:
            prompt = f"""
    User asked:
    
    {query}
    
    The tool returned:
    
    {observation}
    
    Write the final answer for the user.
    """
    
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    
        return response.choices[0].message.content
