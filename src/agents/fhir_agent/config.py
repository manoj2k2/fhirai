import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT", "5672")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_QUEUE = os.environ.get("RABBITMQ_QUEUE", "fhir_queue")

GEMINI_AI_MODEL = os.environ.get("GEMINI_AI_MODEL", "gemini-2.0-flash")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

HAPI_FHIR_URL = os.environ.get("HAPI_FHIR_URL", "http://localhost:8080/fhir")
HAPI_FHIR_VALIDATOR_URL = os.environ.get("HAPI_FHIR_VALIDATOR_URL", "http://localhost:8080/fhir/StructureDefinition")

FHIR_SERVER_URL = os.environ.get("FHIR_SERVER_URL", "http://localhost:8080/fhir")
FHIR_AGENT_PORT = os.environ.get("FHIR_AGENT_PORT", "8001")
