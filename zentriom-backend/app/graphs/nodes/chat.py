from app.services.granite import ask_granite

def chat_node(state):
    response = ask_granite(state["prompt"])
    
    return {
        "result": response
    }