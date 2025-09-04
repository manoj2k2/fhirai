
from langchain_google_genai import GoogleGenerativeAI
from fhir_agent import config


def get_llm():
    """Returns the default LLM provider instance. Can be extended to support multiple providers."""
    return GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=config.GEMINI_API_KEY)
