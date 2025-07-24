from fastapi import APIRouter, HTTPException, status, Depends
from app.auth.auth_handler import get_api_key
from app.schemas.badge_schema import BadgeIssueRequest, BadgeResponse
from app.services.badge_service import issue_badge, verify_badge

router = APIRouter(
    prefix="/badges",
    tags=["Badges"]
)

@router.post("/issue", response_model=BadgeResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_api_key)])
async def issue_badge_route(request: BadgeIssueRequest):
    try:
        badge = await issue_badge(request)
        return badge
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/verify/{badge_id}", response_model=BadgeResponse)
async def verify_badge_route(badge_id: str):
    badge = await verify_badge(badge_id)
    if not badge:
        raise HTTPException(status_code=404, detail="Badge not found or invalid.")
    return badge