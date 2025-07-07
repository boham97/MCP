import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("code-assistant")

@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="generate_code",
            description="Generate code based on prompt",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {"type": "string"}
                },
                "required": ["prompt"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "generate_code":
        # 여기서 로컬 모델 호출
        result = generate_code(arguments["prompt"])
        return [TextContent(type="text", text=result)]

async def main():
    async with stdio_server() as streams:
        await app.run(streams[0], streams[1])

if __name__ == "__main__":
    asyncio.run(main())