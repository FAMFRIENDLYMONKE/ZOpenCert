from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class BadgeIssueRequest(BaseModel):
    recipient_email: EmailStr
    badge_class_url: HttpUrl

class BadgeResponse(BaseModel):
    id: Optional[str]
    badge_id: Optional[str]
    recipient_email_hash: str
    badge_class_url: HttpUrl
    issued_on: datetime
    badge_json: Dict[str, Any]
