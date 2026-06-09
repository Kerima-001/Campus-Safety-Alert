from fastapi import FastAPI

from routes import incidents
from routes import emergency

app = FastAPI(
    title="Campus Safety Alert System"
)

app.include_router(
    incidents.router,
    prefix="/api"
)

app.include_router(
    emergency.router,
    prefix="/api"
)

@app.get("/")

def home():

    return {
        "project":
        "Campus Safety Alert System",
        "status":
        "Running"
    }
