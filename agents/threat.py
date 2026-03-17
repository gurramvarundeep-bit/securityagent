from langchain_openai import ChatOpenAI
from state import SecurityState

llm = ChatOpenAI()

def threat_agent(state: SecurityState):
    event = state["event"]

    result = llm.invoke(f"Classify threat level: {event}")

    return {"threat": result.content}