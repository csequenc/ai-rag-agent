from langchain.tools import tool

@tool
def calculate(expression: str) -> str:
    """
    Use this tool to perform mathematical calculations.
    """
    return str(eval(expression))

print(calculate.name)
print(calculate.description)