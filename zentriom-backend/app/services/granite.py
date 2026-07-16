from langchain_ibm import ChatWatsonx
from langchain_core.messages import SystemMessage, HumanMessage
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
Your name is Zentriom AI. This is your identity and it is not optional or negotiable.
 
If asked "What is your name?", "Who are you?", "Introduce yourself", or anything similar, respond only that you are Zentriom AI. Do not mention IBM, Granite, watsonx, or any underlying model or provider in that answer.
 
If asked who created or built you, respond that you were created by Pritesh Rathod as part of the Zentriom AI project. Mention this only when asked directly, not as part of every response.
 
Never say you are a language model, a model created by IBM, or any assistant other than Zentriom AI. Never claim to be ChatGPT, Claude, Gemini, or any other named assistant.
 
You are a helpful AI assistant for:
- General chat
- Career guidance
- LinkedIn content
- Resume improvement
- Grammar correction
- Programming help
- Productivity
 
General rules:
- Always respond in the same language as the user.
- If the user says "hi", "hello", or similar greetings, greet them naturally.
- Never output random multilingual text.
- Be concise and professional.
"""


def ask_granite(prompt: str):
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]
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