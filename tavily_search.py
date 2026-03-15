
import requests
import os
from typing import List, Dict, Optional

def tavily_search(
    query: str,
    max_results: int = 5,
    search_depth: str = "basic",
    include_answer: bool = True,
    include_images: bool = False,
    include_raw_content: bool = False,
    domains: Optional[List[str]] = None,
    exclude_domains: Optional[List[str]] = None
) -> Dict:
    """
    调用 Tavily AI 搜索 API
    :param query: 搜索关键词
    :param max_results: 最大返回结果数，1-10
    :param search_depth: 搜索深度，basic/advanced
    :param include_answer: 是否包含AI生成的摘要答案
    :param include_images: 是否返回图片结果
    :param include_raw_content: 是否返回页面完整内容
    :param domains: 只搜索指定域名
    :param exclude_domains: 排除指定域名
    :return: 搜索结果字典
    """
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return {"error": "TAVILY_API_KEY 未配置，请先设置环境变量"}
    
    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": max_results,
        "search_depth": search_depth,
        "include_answer": include_answer,
        "include_images": include_images,
        "include_raw_content": include_raw_content
    }
    
    if domains:
        payload["include_domains"] = domains
    if exclude_domains:
        payload["exclude_domains"] = exclude_domains
    
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"搜索请求失败: {str(e)}"}

def format_search_result(result: Dict) -> str:
    """格式化搜索结果为可读文本"""
    if "error" in result:
        return f"❌ 搜索失败: {result['error']}"
    
    output = []
    if result.get("answer"):
        output.append(f"📝 **AI 摘要：** {result['answer']}\n")
    
    output.append("🔍 **搜索结果：**")
    for idx, item in enumerate(result.get("results", []), 1):
        output.append(f"{idx}. [{item['title']}]({item['url']})")
        output.append(f"   摘要：{item['content']}\n")
    
    if result.get("images"):
        output.append("🖼️ **相关图片：**")
        for img in result["images"]:
            output.append(f"- ![{img.get('description', '图片')}]({img['url']})")
    
    return "\n".join(output)

# 测试调用
if __name__ == "__main__":
    result = tavily_search("2026年AI创业热门方向", max_results=3)
    print(format_search_result(result))
