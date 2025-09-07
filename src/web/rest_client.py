import requests

# @aiMapper = http://localhost:8000

# POST {{aiMapper}}/map
# Content-Type: application/json

# {
#   "data": "Practitioner Details: Name: Meera Sahani Gender: Female Qualification: General Practitioner  "
# }
# GET {{aiMapper}}
def call_health_agent_api_Status(api_url: str = "http://localhost:8001") -> dict:
    """
    Calls the health agent REST API endpoint with input data and returns the response as a status.
    Args:
        input_data (str): The normalized data to send to the API.
        api_url (str): The full URL of the API endpoint.
    Returns:
        dict: The JSON response from the API.
    """
    try:
        response = requests.get(api_url )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def call_health_agent_api(input_data: str, api_url: str = "http://localhost:8001/map") -> dict:
    """
    Calls the health agent REST API endpoint with input data and returns the response as a dict.
    Args:
        input_data (str): The normalized data to send to the API.
        api_url (str): The full URL of the API endpoint.
    Returns:
        dict: The JSON response from the API.
    """
    payload = {"normalized_data": input_data}
    try:
        response = requests.post(api_url, json=input_data, 
                                 headers={"Content-Type": "application/json"})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
