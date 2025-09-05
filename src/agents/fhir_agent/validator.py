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

def query_fhir_resource(inputQuery: str, resource_name:str ) -> bool:
    """Validates a FHIR resource using a HAPI FHIR validator."""

    headers = {"Content-Type": "application/fhir+json"}

    response = requests.get(
        f"{config.HAPI_FHIR_URL}/{resource_name}?_format=json&_pretty=true&{inputQuery}",
        headers=headers
    )

    print(f"Query URL: {config.HAPI_FHIR_URL}/{resource_name}?_format=json&_pretty=true&{inputQuery}")  
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")
    
    return response.content