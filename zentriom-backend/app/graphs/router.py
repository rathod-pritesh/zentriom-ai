def router(state):
    
    task = state["task"].lower()
    
    if task == "grammar":
        return "grammar"
    
    if task == "linkedin":
        return "linkedin"
    
    return "chat"