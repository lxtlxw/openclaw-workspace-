import requests
import os
import json

api_key = "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"

query = "戊土生于寅月 天干丙火透出 地支戌未二土 喜用神"

response = requests.post(
    "https://api.tavily.com/search",
    headers={"Content-Type": "application/json"},
    json={
        "api_key": api_key,
        "query": query,
        "max_results": 5,
        "search_depth": "advanced",
        "include_answer": True
    }
)

result = response.json()
print("=== 总结 ===")
print(result.get("answer", "无"))
