from tools import calculate


class Agent:

    def run(self, query):

        if "calculate" in query.lower():
            expression = query.lower().replace("calculate", "").strip()

            result = calculate(expression)

            return result

        return "I don't know how to handle that."
