from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

from src.state import MyState
from src.nodes import call_model, call_tool
from src.edges import should_continue

""" 상태 """
builder = StateGraph(MyState)

""" 정점 """
builder.add_node("call_model", call_model)
builder.add_node("tools", call_tool)

""" 간선 """
builder.add_edge(START, "call_model")
builder.add_conditional_edges("call_model", should_continue, ["tools", END])
builder.add_edge("tools", "call_model")

checkpointer = InMemorySaver()
store = InMemoryStore()
graph = builder.compile(checkpointer, store=store)
