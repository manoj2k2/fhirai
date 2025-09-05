
from fhir_agent import validator, storage
from fastapi import HTTPException
# LangChain and LangGraph imports
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.memory import ConversationBufferMemory
from langgraph.graph import StateGraph, END
from fhir_agent.llm_provider import get_llm
from typing import TypedDict, Optional

import json
import os

def process_fhir_resource(normalized_data: str) -> str:
    """
    Maps normalized data to a FHIR resource using LangChain and LangGraph for AI and human review steps, then validates and stores it.
    Returns a success message if all steps pass, else raises an error.
    """
    # Set up LangChain LLM (OpenAI, can be replaced with other providers)
    llm = get_llm()
    
    # Step 1: AI mapping step

    def ai_mapping_step(state):
        ai_prompt = PromptTemplate(
        input_variables=["normalized_data"],
        template="""
        You are an expert FHIR data mapper. Given the following normalized data, map it to a valid FHIR resource in JSON format. Only output the JSON.
        Normalized data: {normalized_data}
        """ )

        fhir_json = llm(ai_prompt.format(normalized_data=state["normalized_data"]))
        return {"fhir_resource": fhir_json, "normalized_data": state["normalized_data"]}
    # Step 1.1: grab resource type from fhir_json and set resource_type in state
    def set_resource_type_step(state):
        fhir_json_str = state["fhir_resource"]
        # Clean up string if it contains markdown formatting
        fhir_json_str = fhir_json_str.strip().strip("```json").strip("```").strip()
        try:
            fhir_json = json.loads(fhir_json_str)
        except Exception:
            fhir_json = {}
        resourceType = fhir_json.get("resourceType", "Patient")
        state["resource_type"] = resourceType
        return {"fhir_resource": fhir_json_str, "normalized_data": state["normalized_data"], "resource_type": resourceType}
    
    # Step 1.2: grab resource type from fhir_json and set resource_type in state
    def query_resources_setId(state):

        fhir_json_str = state["fhir_resource"]
        resource_type = state["resource_type"]
        # Clean up and parse JSON
        try:
            fhir_json = json.loads(fhir_json_str)
        except Exception:
            fhir_json = {}

        return {"fhir_resource": fhir_json_str, "normalized_data": state["normalized_data"], "resource_type": resource_type}
    

        # Use LLM to generate queries for possible actors (e.g., Patient, Practitioner)
        actor_prompt = PromptTemplate(
            input_variables=["resource_type", "fhir_json_str"],
            template="""
            Given the FHIR resource type {resource_type} and the following FHIR resource JSON:
            {fhir_json_str}
            Identify all dependent resources (e.g., Patient, Practitioner) and generate a FHIR search query for each to find existing resources in the FHIR server. Return a list of queries as array in JSON format, e.g.:
            {{["Patient": "given=manoj", "Practitioner": "given=dr.smith"]}}
            """
        )
        queries_json = llm(actor_prompt.format(resource_type=resource_type, fhir_json_str=fhir_json_str))
        try:
            queries_json = queries_json.strip().strip("```json").strip("```").strip()
            queries = json.loads(queries_json)
        except Exception:
            queries = {}

        # Query FHIR server for each actor and set id for first match
        # '[\n  {\n    "Patient": "?name=Manoj sahani"\n  },\n  {\n    "Patient": "?name=Meera sahani"\n  }\n]'

        for entry in queries:
            if isinstance(entry, dict):
                for actor, query in entry.items():
                    result = validator.query_fhir_resource(query, actor)
                    if result and isinstance(result, list) and len(result) > 0:
                        # Set id in fhir_json for the actor
                        actor_id = result[0].get("id")
                        if actor_id:
                            # Update reference in fhir_json if present
                            if actor in fhir_json:
                                fhir_json[actor]["id"] = actor_id
        # Update state with new fhir_json
        fhir_json_str = json.dumps(fhir_json)
        return {"fhir_resource": fhir_json_str, "normalized_data": state["normalized_data"], "resource_type": resource_type}
    

    # Step 2: Human review step (simulated via LangChain's HumanMessage)
    def human_review_step(state):
        fhir_json = state["fhir_resource"]
        print("\n--- Human Review Required ---\n")
        # remove json from fhir_json and assign to fhir_json
        fhir_json = fhir_json.strip().strip("```json").strip("```").strip()
        print(fhir_json)
        # input("Press Enter to approve, or Ctrl+C to reject and abort...")
        return {"fhir_resource": fhir_json, "normalized_data": state["normalized_data"]}

    # Step 3: Validation step
    def validation_step(state):
        fhir_resource = state["fhir_resource"]
        is_valid = validator.validate_fhir_resource(fhir_resource)
        if not is_valid:
            raise ValueError("Generated FHIR resource is not valid.")
        return {"fhir_resource": fhir_resource, "normalized_data": state["normalized_data"]}

    # Step 4: Storage step
    def storage_step(state):
        fhir_resource = state["fhir_resource"]
        resource_type = state.get("resource_type", "Patient")
        try:
            storage.save_to_fhir_server(fhir_resource, resource_type)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save FHIR resource: {e}")
        return {"message": "FHIR resource created and stored successfully."}

    # Build LangGraph pipeline
    # state_schema = {"normalized_data": str, "fhir_resource": str, "message": str}
 
    workflow = StateGraph(ProcessState)
    workflow.add_node("ai_mapping", ai_mapping_step)    
    workflow.add_node("set_resource_type_step", set_resource_type_step)
    workflow.add_node("query_resources_setId", query_resources_setId)        
    workflow.add_node("human_review", human_review_step)
    workflow.add_node("validation", validation_step)
    workflow.add_node("storage", storage_step)

    workflow.add_edge("ai_mapping", "set_resource_type_step")
    workflow.add_edge("set_resource_type_step", "query_resources_setId")
    workflow.add_edge("query_resources_setId", "human_review")
    workflow.add_edge("human_review", "validation")
    workflow.add_edge("validation", "storage")
    workflow.add_edge("storage", END)

    workflow.set_entry_point("ai_mapping")

    # Run the workflow
    # initial_state = {"normalized_data": normalized_data}
    app = workflow.compile()
    initial_state = ProcessState(normalized_data=normalized_data, fhir_resource="", message="") 

    app.invoke(initial_state)
    return app. initial_state["message"]

class ProcessState(TypedDict):
    normalized_data: str
    fhir_resource: str
    message: str
    resource_type: Optional[str] = "Patient"