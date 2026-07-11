from app.services.linkedin import generate_linkedin_post

def linkedin_node(state):
    
    response = generate_linkedin_post(
        post_type=state["post_type"],
        topic=state["topic"],
        experience=state["experience"],
        tone=state["tone"],
        length=state["length"]
    )
    
    return {
        "result": response
    }