import pytest
from unittest.mock import patch, MagicMock
from fhir_agent.mapper import mapper   

def test_get_fhir_mapping_returns_string():
    test_input = "Patient: John Doe, Male, 1980-01-01"
    expected_output = '{"resourceType": "Patient", "name": [{"family": "Doe", "given": ["John"]}], "gender": "male", "birthDate": "1980-01-01"}'

    with patch("mapper.LLMChain") as mock_chain:
        mock_instance = MagicMock()
        mock_instance.run.return_value = expected_output
        mock_chain.return_value = mock_instance

        result = mapper.get_fhir_mapping(test_input)
        assert isinstance(result, str)
        assert result == expected_output

def test_get_fhir_mapping_handles_empty_input():
    test_input = ""
    expected_output = ""

    with patch("mapper.LLMChain") as mock_chain:
        mock_instance = MagicMock()
        mock_instance.run.return_value = expected_output
        mock_chain.return_value = mock_instance

        result = mapper.get_fhir_mapping(test_input)
        assert result == expected_output

def test_get_fhir_mapping_with_invalid_data():
    test_input = "Random text not related to FHIR"
    expected_output = "Invalid input"

    with patch("mapper.LLMChain") as mock_chain:
        mock_instance = MagicMock()
        mock_instance.run.return_value = expected_output
        mock_chain.return_value = mock_instance

        result = mapper.get_fhir_mapping(test_input)
        assert result