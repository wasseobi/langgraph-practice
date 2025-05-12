import os

from langchain.chat_models import init_chat_model

from src.tools import tools
from src.state import MyState

model = init_chat_model(
    os.getenv("DEFAULT_MODEL"),
    temperature=1.0,
    max_tokens=1024,
)
model_with_tools = model.bind_tools(tools)


def call_model(state: MyState):
    messages = state["messages"]
    response = model_with_tools.invoke(messages)
    print('🤖')
    print(response)
    print()
    return {"messages": [response]}
