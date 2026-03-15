import requests
import os
import json

# 从环境变量获取API key
api_key = os.environ.get("TAVILY_API_KEY")
if not api_key:
    # 从记忆中读取
    api_key = "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"

query = "姓名八字命理 周易取名 核心知识 方法 结合八字五行"

response = requests.post(
    "https://api.tavily.com/search",
    headers={"Content-Type": "application/json"},
    json={
        "api_key": api_key,
        "query": query,
        "max_results": 10,
        "search_depth": "advanced",
        "include_answer": True,
        "include_images": False,
        "include_raw_content": False
    }
)

result = response.json()
print("=== 综合总结 ===")
print(result.get("answer", "无总结"))
print("\n=== 搜索结果 ===")
for i, r in enumerate(result.get("results", [])):
    print(f"{i+1}. {r['title']}")
    print(f"   URL: {r['url']}")
    print(f"   摘要: {r['content'][:200]}...")
    print()

# 保存结果
with open("bazi_search_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
