def router(state):
    
    task = state["task"].lower()
    
    if task == "grammar":
        return "grammar"
    
    if task == "linkedin":
        return "linkedin"
    
    if task == "code_explainer":
        return "code_explainer"
    
    return "chat"