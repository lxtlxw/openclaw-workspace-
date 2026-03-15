import os
import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

api_key = "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"

url = "https://api.tavily.com/search"
query = "daily_stock_analysis GitHub Gemini AI A股智能分析"

payload = {
    "api_key": api_key,
    "query": query,
    "search_depth": "basic",
    "include_answer": True
}

response = requests.post(url, json=payload)
result = response.json()
print(json.dumps(result, indent=2, ensure_ascii=False))
