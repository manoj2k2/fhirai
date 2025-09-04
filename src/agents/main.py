from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from fhir_agent import preprocessor,  feedback
from fhir_agent.fhir_processor import process_fhir_resource

load_dotenv()

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.get("/")
async def get_data():
    return {"message": "FHIR AI Agent is running."}

@app.post("/map")
async def map_data(input_data: InputData):
    """Receives input data, maps it to a FHIR resource, validates it, and stores it."""

    # Preprocess the input data
    normalized_data = preprocessor.normalize(input_data.data)

    # Send the data to RabbitMQ for offline processing
    preprocessor.send_to_rabbitmq(normalized_data)


    # Use the AI agent to map and validate the data to a FHIR resource
    try:
        fhir_resource = process_fhir_resource(normalized_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

class CorrectionData(BaseModel):
    original_data: str
    corrected_fhir_resource: str

@app.post("/correct")
async def correct_mapping(correction_data: CorrectionData):
    """Receives a correction for a mapping."""

    feedback.store_correction(
        correction_data.original_data,
        correction_data.corrected_fhir_resource
    )

    return {"message": "Correction stored successfully."}
