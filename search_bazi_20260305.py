import requests
import os
import json

api_key = "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"

query = "公历2026年3月5日 生辰八字 四柱 干支"

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
print("=== 总结 ===")
print(result.get("answer", "无"))
print("\n=== 结果 ===")
for r in result.get("results", []):
    print(f"{r['title']}")
    print(f"{r['content'][:250]}...")
