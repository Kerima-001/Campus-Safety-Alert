from fastapi import APIRouter

router = APIRouter()

@router.post("/sos")
def emergency_alert():

    return {
        "status": "Emergency Triggered",
        "action": "Campus Police Notified"
    }
