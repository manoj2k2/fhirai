from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from fhir_agent import config

def get_fhir_mapping(data: str) -> str:
    """Uses AI to map input data to a FHIR resource."""
    # Initialize the Google Generative AI model
    llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=config.GEMINI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["data"],
        template="Map the following data to a FHIR resource:\n\n{data}\n\nFHIR Resource:"
    )    

    print("Sending data to AI for FHIR mapping...")
    print(f"Data: {data}")
    chain = LLMChain(llm=llm, prompt=prompt)

    fhir_resource = chain.run(data)
    
    print("Received FHIR resource from AI.")
    print(f"FHIR Resource: {fhir_resource}")

    return fhir_resource


def get_fhir_mapping_Subject(data: str) -> str:
    """Uses AI to map input data to a FHIR resource."""
     
    llm = GoogleGenerativeAI(model=config.GEMINI_AI_MODEL, google_api_key=config.GEMINI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["data"],
        template=""" You are a FHIR-R4 data assistant. 
        Map the following data to a FHIR resource as valid JSON, skip id node. " 
        Convert to FHIR Resource dont use json s root.
        Input text :\n\n{data}\n\n""",
        role="user"    
    )

    print("Sending data to AI for FHIR mapping...")
    print(f"Data: {data}")
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    fhir_resource = chain.run(data)
    
    print("Received FHIR resource from AI.")
    print(f"FHIR Resource: {fhir_resource}")

    return fhir_resource
