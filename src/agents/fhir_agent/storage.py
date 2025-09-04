import requests
from fhir_agent import config


def save_to_fhir_server(resource: str, resurce_type: str = "Patient"):
    """Saves a FHIR resource to a FHIR server."""

    headers = {"Content-Type": "application/fhir+json"}

    response = requests.post(
        f"{config.FHIR_SERVER_URL}/{resurce_type}",
        data=resource,
        headers=headers
    )

    response.raise_for_status()
