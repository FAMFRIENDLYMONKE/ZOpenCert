from fastapi import APIRouter, HTTPException, status
from app.schemas.certificate_schema import CertificateIssueRequest, CertificateResponse
from app.services.blockcerts_service import issue_certificate, verify_certificate

router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"]
)

@router.post("/issue", response_model=CertificateResponse, status_code=status.HTTP_201_CREATED)
async def issue_certificate_route(request: CertificateIssueRequest):
    try:
        certificate = await issue_certificate(request)
        return certificate
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify", response_model=CertificateResponse)
async def verify_certificate_route(certificate_json: dict):
    try:
        verified = await verify_certificate(certificate_json)
        if not verified:
            raise HTTPException(status_code=400, detail="Certificate verification failed.")
        return verified
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
