import yaml
from typing import Any

with open("src/hapi_mcpserver/hapi_openapi.yaml", "r", encoding="utf-8") as f:
    openapi = yaml.safe_load(f)
FHIR_BASE = "http://localhost:8080/fhir"

print("# MCP tool stubs for all FHIR resources with descriptions and type bindings")
print("from fastmcp import FastMCP")
print("import requests")
print("from typing import Dict, Any, Optional")
print()
print('FHIR_BASE = "http://localhost:8080/fhir"')
print("mcp = FastMCP('My MCP Server')\n")

for path, path_item in openapi.get("paths", {}).items():
    for method, op in path_item.items():
        op_id = op.get("operationId", None)
        summary = op.get("summary", "")
        description = op.get("description", "")
        params = op.get("parameters", [])
        request_body = op.get("requestBody", None)
        tag = op.get("tags", [""])[0]
        # Build function name
        func_name = op_id or f"{method}_{tag.lower()}"
        # Build parameter list
        param_list = []
        param_doc = []
        for param in params:
            pname = param["name"]
            ptype = "str"
            if param.get("schema", {}).get("type") == "integer":
                ptype = "int"
            elif param.get("schema", {}).get("type") == "boolean":
                ptype = "bool"
            param_list.append(f"{pname}: {ptype}")
            param_doc.append(f"    :param {pname}: {param.get('description', '')}")
        if request_body:
            param_list.append("body: dict")
            param_doc.append("    :param body: Request body as dict")
        param_str = ", ".join(param_list) if param_list else ""
        # Build docstring
        docstring = f'"""{summary}\n{description}\n' + "\n".join(param_doc) + '\n"""'
        # Build HTTP call
        if method == "get":
            call = f'resp = requests.get(F"{FHIR_BASE}{path}", params={{'
            call += ", ".join([f'"{p["name"]}": {p["name"]}' for p in params])
            call += "})"
        elif method in ("post", "put"):
            call = f'resp = requests.{method}(F"{FHIR_BASE}{path}", json=body)'
        else:
            call = f'# Not implemented: {method.upper()} {path}'
        # Print function
        print(f"@mcp.tool")
        print(f"def {func_name}({param_str}) -> Dict[str, Any]:")
        print(f"    {docstring}")
        print(f"    {call}")
        print(f"    return resp.json()\n")

print("if __name__ == '__main__':")
print("    mcp.run(host='0.0.0.0', port=8085)")