from typing import TypedDict

class SecurityState(TypedDict):
    event: str
    threat: str
    intel: str
    response: str
    final_report: str