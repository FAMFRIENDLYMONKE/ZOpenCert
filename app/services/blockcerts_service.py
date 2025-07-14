from app.schemas.certificate_schema import CertificateIssueRequest, CertificateResponse
import subprocess
import json
import uuid
from datetime import datetime, timezone
from app.database import certificate_collection

async def issue_certificate(request: CertificateIssueRequest) -> CertificateResponse:
    certificate_id = str(uuid.uuid4())

    try:
        subprocess.run([
            "cert-tools",
            "create-certificate",
            "--template", "path/to/template.json",
            "--recipient", request.recipient_email,
            "--output", f"./issued/{certificate_id}.json"
        ], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Cert-tools generation failed: {e}")

    try:
        subprocess.run([
            "cert-issuer",
            "-c", "path/to/conf.ini"
        ], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Cert-issuer failed: {e}")

    with open(f"./issued/{certificate_id}.json", "r") as f:
        cert_json = json.load(f)

    await certificate_collection.insert_one(cert_json)

    response = CertificateResponse(
        certificate_id=certificate_id,
        recipient=request.recipient_email,
        issued_on=datetime.now(timezone.utc),
        blockchain_txid=cert_json.get("signature", {}).get("anchors", [{}])[0].get("sourceId"),
        certificate_json=cert_json
    )
    return response

async def verify_certificate(certificate_json: dict) -> CertificateResponse:
    blockchain_txid = certificate_json.get("signature", {}).get("anchors", [{}])[0].get("sourceId")
    if not blockchain_txid:
        return None

    # Optionally: call blockchain API or Blockcerts verifier here

    response = CertificateResponse(
        certificate_id=certificate_json.get("id"),
        recipient=certificate_json.get("recipient", {}).get("identity"),
        issued_on=certificate_json.get("issuedOn"),
        blockchain_txid=blockchain_txid,
        certificate_json=certificate_json
    )
    return response