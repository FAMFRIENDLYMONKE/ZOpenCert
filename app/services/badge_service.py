from app.schemas.badge_schema import BadgeIssueRequest, BadgeResponse
# from app.utils.digital_sign import sign_data
import hashlib
import uuid
from datetime import datetime, timezone
from app.database import badge_collection

async def issue_badge(request: BadgeIssueRequest) -> BadgeResponse:
    salt = "8612807198" #generated using true random generator
    recipient_hash = hashlib.sha256((request.recipient_email + salt).encode()).hexdigest()

    badge_id = str(uuid.uuid4())

    badge_json = {
        "@context": "https://w3id.org/openbadges/v2",
        "type": "Assertion",
        "id": f"https://zcertify.zairza.co.in/badges/{badge_id}",
        "recipient": {
            "type": "email",
            "hashed": True,
            "salt": salt,
            "identity": recipient_hash
        },
        "badge": request.badge_class_url,
        "verification": {
            "type": "HostedBadge"
        },
        "issuedOn": datetime.now(timezone.utc)
    }

    # signature = sign_data(badge_json)
    # badge_json["signature"] = signature

    await badge_collection.insert_one(badge_json)

    return BadgeResponse(**badge_json)

async def verify_badge(badge_id: str) -> BadgeResponse:
    badge = await badge_collection.find_one({"id": f"https://yourdomain.com/badges/{badge_id}"})

    if not badge:
        return None

    # is_valid = verify_signature(badge, badge["signature"])
    # if not is_valid:
    #     return None

    return BadgeResponse(**badge)
