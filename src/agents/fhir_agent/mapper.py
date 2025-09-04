
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from  agents.fhir_agent.llm_provider import llms

 
def get_fhir_mapping(data: str, llm=None) -> str:
    """Uses AI to map input data to a FHIR resource. Accepts an optional LLM provider."""
    if llm is None:
        llm = llms.get_llm()

    prompt = PromptTemplate(
        input_variables=["data"],
        template="""Map the following data to a FHIR resource:\n\n{data}\n\nFHIR Resource:
        return only the FHIR resource in JSON format. Json shall be compatible with FHIR R4.
        """,
    )

    print("Sending data to AI for FHIR mapping...")
    print(f"Data: {data}")
    chain = LLMChain(llm=llm, prompt=prompt)

    fhir_resource = chain.run(data)
    
    print("Received FHIR resource from AI.")
    print(f"FHIR Resource: {fhir_resource}")

    return fhir_resource
