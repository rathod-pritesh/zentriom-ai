from langgraph.graph import StateGraph, END

from app.graphs.state import AIState
from app.graphs.router import router

from app.graphs.nodes.chat import chat_node
from app.graphs.nodes.grammar import grammar_node
from app.graphs.nodes.linkedin import linkedin_node
from app.graphs.nodes.code_explainer import code_explainer_node

builder = StateGraph(AIState)

builder.add_node("chat", chat_node)
builder.add_node("grammar", grammar_node)
builder.add_node("linkedin", linkedin_node)
builder.add_node("code_explainer", code_explainer_node)

builder.set_conditional_entry_point(
    router,
    {
        "chat": "chat",
        "grammar": "grammar",
        "linkedin": "linkedin",
        "code_explainer": "code_explainer"
    }
)

builder.add_edge("chat", END)
builder.add_edge("grammar", END)
builder.add_edge("linkedin", END)
builder.add_edge("code_explainer", END)

graph = builder.compile()