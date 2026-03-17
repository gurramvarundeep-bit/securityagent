from state import SecurityState

def reflection_agent(state: SecurityState):

    report = f"""
Threat: {state['threat']}
Intel: {state['intel']}
Response: {state['response']}
"""

    return {"final_report": f"Refined Report:\n{report}"}