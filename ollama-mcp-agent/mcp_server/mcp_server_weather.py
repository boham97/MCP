from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

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
    url = "https://korean.visitseoul.net/weather"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 3일 예보 테이블 찾기
    table = soup.select_one("div.tb_weather.tb_scroll table")

    # 날짜 (thead 안)
    dates = [th.get_text(strip=True) for th in table.select("thead th")[1:]]  # 첫번째 "항목" 제외

    # tbody 행별 데이터
    rows = table.select("tbody tr")

    # 데이터 구조화
    forecast = {d: {} for d in dates}
    result = ""
    for row in rows:
        label = row.select_one("th").get_text(strip=True)
        cols = row.select("td")
        for i, col in enumerate(cols):
            forecast[dates[i]][label] = col.get_text(" ", strip=True)

    # 결과 출력
    for day, info in forecast.items():
        result += f"{day}\n"
        for key, value in info.items():
            result += f"  • {key}: {value}\n"
        result += "\n"
    
    return result.strip()


if __name__ == "__main__":
    mcp.run(transport="stdio")