from fastapi import APIRouter, Depends
from app.services.history_service import save_history
from app.schemas.linkedin import LinkedInRequest
from app.graphs.workflow import graph

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.core.dependencies import (
    get_current_user
)

from app.models.users import User

router = APIRouter()

@router.post("/linkedin")
def linkedin(
    data: LinkedInRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = graph.invoke({
        "task": "linkedin",
        "post_type": data.post_type,
        "topic": data.topic,
        "experience": data.experience,
        "tone": data.tone,
        "length": data.length
    })
    
    save_history(
        db=db,
        user_id=current_user.id,
        category="linkedin",
        title=data.topic,
        input_text=data.experience,
        output_text=result["result"]
    )

    
    return {
        "post": result["result"]
    }