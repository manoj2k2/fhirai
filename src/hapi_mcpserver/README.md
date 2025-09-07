& cd "C:\Users\aryan\source\repos\fhirai\src\hapi_mcoserver" 
 fastmcp run main.py:mcp --transport http --port 8085
& cd "C:\Users\aryan\source\repos\fhirai\src\hapi_mcoserver" & python client.py

 fastmcp run hapi_mcp.py:mcp --transport http --port 8085

& C:/Users/aryan/source/repos/fhirai/.venv/Scripts/python.exe src/hapi_mcpserver/generate_mcp_tools.py > mcptool3.txt

npx modelcontextprotocol/inspector