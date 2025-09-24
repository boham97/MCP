from mcp.server.fastmcp import FastMCP
import requests

# Initialize FastMCP server with configuration
mcp = FastMCP(
    "Weather",  # Name of the MCP server
    instructions="You are a weather assistant that can answer questions about the weather in a given location.",  # Instructions for the LLM on how to use this tool
    host="0.0.0.0",  # Host address (0.0.0.0 allows connections from any IP)
    port=8005,  # Port number for the server
)

@mcp.tool()
async def get_weather_forecast() -> str:
    """
    Get mid-term weather forecast from a predefined URL.
    Returns:
        str: A string containing the weather forecast information
    """
    url = f"https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=109"
    
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"오류: {e}"

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get current weather information for the specified location.

    Args:
        location (str): The name of the location (city, region, etc.) to get weather for

    Returns:
        str: A string containing the weather information for the specified location
    """
    # Return a mock weather response
    # In a real implementation, this would call a weather API
    print(f"\n[DEBUG] MCP: get_weather called: {location}\n")
    return f"오전은 비, 오후는 맑음. 최고기온 19도, 최저기온 8도. 동남풍 2~3m/s 예상. 강우량 2mm 이하. {location} 날씨 예보입니다."


if __name__ == "__main__":
    mcp.run(transport="stdio")