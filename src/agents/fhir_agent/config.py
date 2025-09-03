import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "fhir_queue")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY","")
GEMINI_AI_MODEL = os.getenv("GEMINI_AI_MODEL","gemini-2.0-flash")

HAPI_FHIR_VALIDATOR_URL = os.getenv("HAPI_FHIR_VALIDATOR_URL", "http://localhost:8080/fhir/StructureDefinition")

FHIR_SERVER_URL = os.getenv("FHIR_SERVER_URL", "http://localhost:8080/fhir")
