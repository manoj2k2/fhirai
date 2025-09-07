

from fastmcp import FastMCP
from pydantic import BaseModel
from typing import Dict, Any
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!" 
 
# Patient resource
class PatientResource(BaseModel):
    id: str
    name: str
    gender: str
    birthDate: str

# Practitioner resource
class PractitionerResource(BaseModel):
    id: str
    name: str
    specialty: str

# Appointment resource
class AppointmentResource(BaseModel):
    id: str
    patient_id: str
    practitioner_id: str
    date: str

@mcp.tool
def create_patient(patient: PatientResource) -> Dict[str, Any]:
    # Add logic to store or forward patient to HAPI REST API
    # Example bridge: POST to HAPI REST API
    try:
        resp = requests.post("http://localhost:8080/fhir/Patient", json=patient.dict())
        return {"message": "Patient created via bridge", "response": resp.json()}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool
def create_practitioner(practitioner: PractitionerResource) -> Dict[str, Any]:
    try:
        resp = requests.post("http://localhost:8080/fhir/Practitioner", json=practitioner.dict())
        return {"message": "Practitioner created via bridge", "response": resp.json()}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool
def create_appointment(appointment: AppointmentResource) -> Dict[str, Any]:
    try:
        resp = requests.post("http://localhost:8080/fhir/Appointment", json=appointment.dict())
        return {"message": "Appointment created via bridge", "response": resp.json()}
    except Exception as e:
        return {"error": str(e)}

# Bridge tool for generic HAPI REST API calls
@mcp.tool
def hapi_bridge(resource_type: str, data: dict, method: str = "POST") -> Dict[str, Any]:
    url = f"http://localhost:8080/fhir/{resource_type}"
    try:
        if method.upper() == "POST":
            resp = requests.post(url, json=data)
        elif method.upper() == "GET":
            resp = requests.get(url, params=data)
        else:
            return {"error": "Unsupported method"}
        return {"status_code": resp.status_code, "response": resp.json()}
    except Exception as e:
        return {"error": str(e)}

# Server info tool
@mcp.tool
def server_info() -> Dict[str, Any]:
    return {
        "server": "FastMCP Example Server",
        "resources": ["Patient", "Practitioner", "Appointment"],
        "status": "running",
        "bridge": "HAPI REST API bridge available"
    }

# Optionally, add more endpoints or custom logic here

if __name__ == "__main__":
   mcp.run(host="0.0.0.0", port=8085)
            
