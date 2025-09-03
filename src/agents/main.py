from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from fhir_agent import preprocessor, mapper, validator, storage, feedback

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

    # Use the AI agent to map the data to a FHIR resource
    fhir_resource = mapper.get_fhir_mapping_Subject(normalized_data)

    # Validate the FHIR resource
    is_valid = validator.validate_fhir_resource(fhir_resource)

    if not is_valid:
        raise HTTPException(status_code=400, detail="Generated FHIR resource is not valid.")

    # Store the FHIR resource
    try:
        storage.save_to_fhir_server(fhir_resource)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save FHIR resource: {e}")

    return {"message": "FHIR resource created and stored successfully."}

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
