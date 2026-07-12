from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt, JWTError

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.users import User

from app.core.config import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM
)

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )
        
        user_id = payload.get("sub")
        
        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
            
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
        
    user =  (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
        
    return user