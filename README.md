# MCP
mcp server with open source for C, JAVA


pip >= 25.1.1
Requires-Python >=3.10

LLM <---> MCP client <--> MCP server
                     <--->MCp server

MCP client 필요
```
pip install uv
pip install ollmcp
ollmcp --servers-json config.json --model qwen2.5:7b
```

`config.json` 에 MCP 서버 정보를 넣어줘야함