import requests
from fhir_agent import config

def create_fhir_resource(resource: str,  resourcename: str) -> bool:
    """Validates a FHIR resource using a HAPI FHIR validator."""

    headers = {"Content-Type": "application/fhir+json"}

    response = requests.post(
        f"{config.FHIR_SERVER_URL}/{resourcename}",
        data=resource,
        headers=headers
    )

    return response.status_code == 200
