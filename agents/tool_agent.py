# Tool Executor Agent

from tools.calculator import calculate

class ToolAgent:
    def execute(self, tool_name, input_value):
        if tool_name == "calculator":
            return calculate(input_value)
        return "Tool not allowed"
