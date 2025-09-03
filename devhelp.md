# Developer Help: fhir_agent

This guide provides essential commands for building, installing dependencies, running, and testing the `fhir_agent` project.

## 1. Build (Docker Compose)

```
docker compose -f infra/docker-compose.yml up -d --build
```

## 2. Install Python Dependencies

(Recommended: Use a virtual environment)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r src/agents/pyproject.toml

pip install -e ./src/agents
```

Or, if using `requirements.txt` (if available):

```
pip install -r requirements.txt
```

## 3. Run the FastAPI Server

```
cd src/agents
uvicorn fhir_agent.main:app --reload
```

## 4. Run Tests

```
pytest src/fhir-agent/Testcase/test_mapper.py
```

Or to run all tests:

```
pytest
```

---

**Note:**
- Ensure all required environment variables are set (see `src/agents/fhir_agent/config.py`).
- For RabbitMQ and FHIR server, use Docker Compose as above.
- For development, activate your virtual environment before running commands.
