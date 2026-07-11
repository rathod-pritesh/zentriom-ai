from typing import TypedDict

class AIState(TypedDict):
    task: str
    prompt: str
    
    post_type: str
    topic: str
    experience: str
    tone: str
    length: str
    
    result: str