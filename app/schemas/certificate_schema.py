from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class CertificateIssueRequest(BaseModel):
    recipient_email: EmailStr
    course_name: str
    issue_date: Optional[datetime] = None

class CertificateResponse(BaseModel):
    certificate_id: str
    recipient: str
    issued_on: datetime
    blockchain_txid: Optional[str]
    certificate_json: Dict[str, Any]