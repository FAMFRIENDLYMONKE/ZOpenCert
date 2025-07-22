from pydantic import BaseModel, HttpUrl, EmailStr, Field, BeforeValidator
from typing import Dict, Any, Optional, Annotated
from datetime import datetime

class BadgeIssueRequest(BaseModel):
    recipient_email: EmailStr
    recipient_name: str
    badge_class_url: HttpUrl
    

PyObjectId = Annotated[str, BeforeValidator(str)]
class BadgeResponse(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    badge_id: str
    recipient_name: str
    badge_class_url: str
    issued_on: datetime
    badge_json: Dict[str, Any]

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        json_encoders = {HttpUrl: str}
