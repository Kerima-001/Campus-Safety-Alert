from fastapi import APIRouter

router = APIRouter()

incidents = []

@router.post("/incident")

def create_incident(data: dict):

    incidents.append(data)

    return {
        "message": "Incident Submitted",
        "incident": data
    }

@router.get("/incident")

def get_incidents():

    return incidents
