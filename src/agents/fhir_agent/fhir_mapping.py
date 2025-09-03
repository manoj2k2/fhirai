from fhir_agent import mapper, validator

def map_and_validate_fhir_resource(normalized_data: str) -> str:
    """
    Maps normalized data to a FHIR resource using the AI agent and validates it.
    Returns the FHIR resource JSON string if valid, else raises ValueError.
    """
    fhir_resource = mapper.get_fhir_mapping_Subject(normalized_data)
    is_valid = validator.validate_fhir_resource(fhir_resource)
    if not is_valid:
        raise ValueError("Generated FHIR resource is not valid.")
    return fhir_resource