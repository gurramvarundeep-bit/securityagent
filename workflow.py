from agents.threat import threat_agent
from agents.intel import intel_agent
from agents.response import response_agent
from agents.reflection import reflection_agent

def run_security_analysis(event: str):

    state = {"event": event}

    state.update(threat_agent(state))
    state.update(intel_agent(state))
    state.update(response_agent(state))
    state.update(reflection_agent(state))

    return state["final_report"]