import os
from typing import Dict, List
from langchain.schema import AIMessage, HumanMessage
from langchain.chat_models import init_chat_model

from src.tools import tools
from src.state import ChatState

model = init_chat_model(
    os.getenv("DEFAULT_MODEL"),
    temperature=1.0,
    max_tokens=1024,
)
model_with_tools = model.bind_tools(tools)

def filter_empty_messages(messages: List) -> List:
    """빈 내용의 메시지를 필터링합니다."""
    return [msg for msg in messages if (
        isinstance(msg, (HumanMessage, AIMessage)) and 
        msg.content and 
        msg.content.strip()
    )]

def format_response(response: AIMessage) -> Dict:
    """모델 응답을 표준 형식으로 변환합니다."""
    return {
        "messages": [response],
        "reply": response.content if response.content else "",
        "action_required": hasattr(response, "additional_kwargs") and bool(response.additional_kwargs.get("tool_calls")),
        "executed_result": response.additional_kwargs if hasattr(response, "additional_kwargs") else {}
    }

def call_model(state: ChatState):
    messages = state["messages"]
    
    # 빈 메시지 필터링
    filtered_messages = filter_empty_messages(messages)
    if not filtered_messages:
        return {
            "messages": messages,
            "reply": "메시지가 비어있습니다.",
            "action_required": False,
            "executed_result": {}
        }
    
    # 모델 호출 및 응답 처리
    try:
        response = model_with_tools.invoke(filtered_messages)
        print('🤖 모델 응답:')
        print(response)
        print()
        return format_response(response)
    except Exception as e:
        print(f"모델 호출 중 오류 발생: {str(e)}")
        return {
            "messages": messages,
            "reply": f"모델 호출 중 오류가 발생했습니다: {str(e)}",
            "action_required": False,
            "executed_result": {"error": str(e)}
        }
