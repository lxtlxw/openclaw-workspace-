import requests
import os

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

result = tavily_search("OpenClaw agent-browser skill 使用方法", max_results=5)
print("AI总结：\n", result["answer"])
print("\n搜索结果：")
for r in result["results"]:
    print(f"- {r['title']}: {r['url']}")
    print(f"  摘要：{r['content'][:300]}...\n")
