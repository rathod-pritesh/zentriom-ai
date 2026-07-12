from typing import TypedDict

class AIState(TypedDict, total=False):
    task: str
    prompt: str
    
    post_type: str
    topic: str
    experience: str
    tone: str
    length: str
    
    code: str
    language: str
    
    result: str