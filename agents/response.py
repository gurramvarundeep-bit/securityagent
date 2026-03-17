from state import SecurityState

def response_agent(state: SecurityState):
    threat = state["threat"]

    return {"response": f"Recommended actions for: {threat}"}