from state import SecurityState

def intel_agent(state: SecurityState):
    event = state["event"]

    return {"intel": f"External intel for: {event}"}