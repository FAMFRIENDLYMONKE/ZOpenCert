from app.schemas.badge_schema import BadgeIssueRequest, BadgeResponse
# from app.utils.digital_sign import sign_data
import hashlib
import uuid
from datetime import datetime, timezone
from app.database import get_badge_collection
from typing import Optional

async def issue_badge(request: BadgeIssueRequest) -> BadgeResponse:
    badge_collection = get_badge_collection()

    badge_id = str(uuid.uuid4())
    salt = "0527974201"
    recipient_hash = hashlib.sha256((request.recipient_email + salt).encode()).hexdigest()

    issued_on = datetime.now(timezone.utc)

    badge_json = {
        "@context": "https://w3id.org/openbadges/v2",
        "id": f"https://zcertify.zairza.co.in/badges/{badge_id}",
        "type": "Assertion",
        "recipient": {
            "type": "email",
            "salt": salt,
            "hashed": True,
            "identity": recipient_hash
        },
        "badge": str(request.badge_class_url).replace("http://", "https://"),
        "verification": {
            "type": "hosted"
        },
        "issuedOn": issued_on,
    }

    # signature = sign_data(badge_json)
    
    db_data = {
        "badge_id": badge_id,
        "recipient_name": request.recipient_name,
        "badge_class_url": str(request.badge_class_url),
        "issued_on": issued_on,
        "badge_json": badge_json
    }

    badge = await badge_collection.insert_one(db_data)

    response_data = {
        "id": badge.inserted_id,
        **db_data
    }
    return BadgeResponse(**response_data)


async def verify_badge(badge_id: str) -> Optional[BadgeResponse]:
    badge = await get_badge_collection().find_one({"badge_id": badge_id})

    if not badge:
        return None

    # is_valid = verify_signature(badge, badge["signature"])
    # if not is_valid:
    #     return None

    return BadgeResponse(**badge)
