import requests
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.environ["TAVILY_API_KEY"] = "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"

def tavily_search(query, max_results=5):
    api_key = os.environ.get("TAVILY_API_KEY")
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Content-Type": "application/json"},
        json={
            "api_key": api_key,
            "query": query,
            "max_results": max_results,
            "search_depth": "advanced",
            "include_answer": True,
            "include_images": False,
            "include_raw_content": False
        }
    )
    return response.json()

# 搜索OpenClaw推荐技能，选一个新的学习
query = "OpenClaw 必装实用技能推荐 2026"
result = tavily_search(query, max_results=5)
print("搜索总结：\n", result["answer"])
print("\n推荐技能：")
for r in result["results"]:
    print(f"- {r['title']}: {r['url']}")
    print(f"  摘要：{r['content'][:300]}...\n")
