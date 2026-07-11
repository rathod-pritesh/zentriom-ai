from app.services.granite import ask_granite

def grammar_node(state):
    
    prompt=f"""
    Correct grammar only.

Text:
{state["prompt"]}
    """
    
    response = ask_granite(prompt)
    
    return {
        "result": response
    }