import yaml
with open("src/hapi_mcpserver/hapi_openapi.yaml", "r", encoding="utf-8") as f:
    openapi = yaml.safe_load(f)

import yaml
with open("src/hapi_mcpserver/hapi_openapi.yaml", "r", encoding="utf-8") as f:
    openapi = yaml.safe_load(f)

resource_names = []
resource_desc = {}
for tag in openapi.get("tags", []):
    if "FHIR resource type" in tag.get("description", ""):
        resource_names.append(tag["name"])
        resource_desc[tag["name"]] = tag.get("description", "")

print("# MCP tool stubs for all FHIR resources with descriptions")
print("from fastmcp import FastMCP")
print("import requests")
print("from typing import Dict, Any")
print()
print('FHIR_BASE = "http://localhost:8080/fhir"')
print("mcp = FastMCP('My MCP Server')\n")

for resource in resource_names:
    desc = resource_desc.get(resource, "")
    print(f"@mcp.tool")
    print(f"def create_{resource.lower()}(data: dict) -> Dict[str, Any]:")
    print(f'    """Create a {resource}. {desc}"""')
    print(f"    resp = requests.post(f'{{FHIR_BASE}}/{resource}', json=data)")
    print(f"    return resp.json()\n")
    print(f"@mcp.tool")
    print(f"def get_{resource.lower()}(resource_id: str) -> Dict[str, Any]:")
    print(f'    """Get a {resource} by ID. {desc}"""')
    print(f"    resp = requests.get(f'{{FHIR_BASE}}/{resource}/{{resource_id}}')")
    print(f"    return resp.json()\n")
    print(f"@mcp.tool")
    print(f"def search_{resource.lower()}(params: dict) -> Dict[str, Any]:")
    print(f'    """Search {resource} resources. {desc}"""')
    print(f"    resp = requests.get(f'{{FHIR_BASE}}/{resource}', params=params)")
    print(f"    return resp.json()\n")

print("if __name__ == '__main__':")
print("    mcp.run(host='0.0.0.0', port=8085)")