from langgraph.graph import END
from src.state import MyState


def should_continue(state: MyState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END
