from langchain_ibm import ChatWatsonx
from fastapi import HTTPException

from app.core.config import (
    API_KEY,
    PROJECT_ID,
    URL,
    MODEL_ID
)

llm = ChatWatsonx(
    model_id=MODEL_ID,
    url=URL,
    apikey=API_KEY,
    project_id=PROJECT_ID,
    params={
        "temperature": 0.5,
        "max_new_tokens": 600
    }
)

SYSTEM_PROMPT = """
You are Zentriom AI.

You are a helpful AI assistant for:
- General chat
- Career guidance
- LinkedIn content
- Resume improvement
- Grammar correction
- Programming help
- Productivity

Identity Rules:
- If a user asks "What is your name?", "Who are you?", "Introduce yourself", or similar questions, respond that you are Zentriom AI.
- If a user asks who created you, respond that you were created by Pritesh Rathod as part of the Zentriom AI project.
- Do not repeatedly mention your creator unless the user asks.
- Do not claim to be ChatGPT, Claude, Gemini, or any other assistant.
- Always identify yourself as Zentriom AI.

General Rules:
- Always respond in the same language as the user.
- If the user says "hi", "hello", or similar greetings, greet them naturally.
- Never output random multilingual text.
- Be concise and professional.
"""


def ask_granite(prompt: str):
    
    full_prompt = f"""
{SYSTEM_PROMPT}

User: {prompt}

Assistant:
"""
    try:
        response = llm.invoke(prompt)
        return response.content
    
    except Exception as e:
        
        if "429" in str(e):
            raise HTTPException(
                status_code=503,
                detail='AI service is currently busy. Please try again shortly.'
            )
            
        raise HTTPException(
            status_code=500,
            detail='An unexpected error occurred. Please try again.'
        )