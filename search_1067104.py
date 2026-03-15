import requests
import os

api_key = "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"

query = "流放之路2 登录失败 错误码 1067104 解决方法"

response = requests.post(
    "https://api.tavily.com/search",
    headers={"Content-Type": "application/json"},
    json={
        "api_key": api_key,
        "query": query,
        "max_results": 5,
        "search_depth": "basic",
        "include_answer": True,
        "include_images": False,
        "include_raw_content": False
    }
)

result = response.json()
print("=== 搜索总结 ===")
print(result.get("answer", "无总结"))
print("\n=== 搜索结果 ===")
for r in result.get("results", []):
    print(f"- {r['title']}: {r['url']}")
    print(f"  摘要: {r.get('content', '')[:200]}...")
