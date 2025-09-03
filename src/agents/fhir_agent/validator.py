import requests
from fhir_agent import config

def validate_fhir_resource(resource: str) -> bool:
    """Validates a FHIR resource using a HAPI FHIR validator."""

    headers = {"Content-Type": "application/fhir+json"}

    response = requests.post(
        f"{config.HAPI_FHIR_VALIDATOR_URL}/$validate",
        data=resource,
        headers=headers
    )

    return response.status_code == 200
