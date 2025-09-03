import requests
from fhir_agent import config

def save_to_fhir_server(resource: str):
    """Saves a FHIR resource to a FHIR server."""

    headers = {"Content-Type": "application/fhir+json"}

    response = requests.post(
        config.FHIR_SERVER_URL,
        data=resource,
        headers=headers
    )

    response.raise_for_status()
