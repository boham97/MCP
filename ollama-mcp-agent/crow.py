import requests
from bs4 import BeautifulSoup

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

for day, info in forecast.items():
    result += f"{day}\n"
    for key, value in info.items():
        result += f"  • {key}: {value}\n"
    result += "\n"

print( result.strip())
