import requests
import os

# Set API key from memory
os.environ["TAVILY_API_KEY"] = "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"

def tavily_search(query, max_results=5):
    """Search web using Tavily API"""
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return "Error: TAVILY_API_KEY not set"
    
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Content-Type": "application/json"},
        json={
            "api_key": api_key,
            "query": query,
            "max_results": max_results,
            "search_depth": "basic",
            "include_answer": True,
            "include_images": False,
            "include_raw_content": False
        }
    )
    return response.json()

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Search for tomorrow's stock recommendation
result = tavily_search("2026年3月12日A股开盘推荐买入股票 热门潜力股", max_results=5)
print("AI总结：\n", result["answer"])
print("\n搜索结果：")
for r in result["results"]:
    print(f"- {r['title']}: {r['url']}")
    if 'content' in r:
        print(f"  摘要：{r['content'][:200]}...\n")
