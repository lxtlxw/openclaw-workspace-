import requests
import os
import json

api_key = "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"

query = "2026年惊蛰交节时间 公历几点"

response = requests.post(
    "https://api.tavily.com/search",
    headers={"Content-Type": "application/json"},
    json={
        "api_key": api_key,
        "query": query,
        "max_results": 5,
        "search_depth": "basic",
        "include_answer": True
    }
)

result = response.json()
print("结果：")
print(result.get("answer", "无"))
for r in result.get("results", []):
    print(f"- {r['title']}: {r['url']}")
    print(f"  {r['content'][:150]}...")
