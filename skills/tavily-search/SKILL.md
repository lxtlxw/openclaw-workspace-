---
name: tavily-search
description: "Tavily AI search for real-time web search. Use when: (1) current information needed, (2) research topics, (3) fact-checking, (4) finding latest news, (5) web content extraction. Requires TAVILY_API_KEY environment variable."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
        "requires": { "env": ["TAVILY_API_KEY"] },
        "install": []
      }
  }
---

# Tavily Search Skill

AI-powered web search with real-time results.

## When to Use

✅ **USE this skill when:**

- Need current/real-time information
- Researching topics
- Fact-checking claims
- Finding latest news
- Web content extraction
- Competitive research

## When NOT to Use

❌ **DON'T use this skill when:**

- General knowledge (use model's training data)
- Simple calculations (use calculator)
- Code generation (use coding-agent)
- File operations (use file tools)

## Setup

```bash
# Set API key
export TAVILY_API_KEY="tvly-xxxxxxxx"
```

Get API key at: https://tavily.com

## API Usage

### Basic Search

```python
import requests
import os

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
            "search_depth": "basic",  # or "advanced"
            "include_answer": True,
            "include_images": False,
            "include_raw_content": False
        }
    )
    return response.json()

# Example
result = tavily_search("latest AI news 2024")
print(result["answer"])
for r in result["results"]:
    print(f"- {r['title']}: {r['url']}")
```

### Advanced Search

```python
def tavily_advanced_search(query, domains=None, exclude_domains=None):
    """Advanced search with domain filtering"""
    api_key = os.environ.get("TAVILY_API_KEY")
    
    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": 10,
        "search_depth": "advanced",
        "include_answer": True,
        "include_raw_content": True,
    }
    
    if domains:
        payload["include_domains"] = domains
    if exclude_domains:
        payload["exclude_domains"] = exclude_domains
    
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Content-Type": "application/json"},
        json=payload
    )
    return response.json()

# Search only specific sites
result = tavily_advanced_search(
    "machine learning",
    domains=["arxiv.org", "paperswithcode.com"]
)
```

### Extract Content

```python
def tavily_extract(url):
    """Extract content from a URL"""
    api_key = os.environ.get("TAVILY_API_KEY")
    
    response = requests.post(
        "https://api.tavily.com/extract",
        headers={"Content-Type": "application/json"},
        json={
            "api_key": api_key,
            "urls": [url],
            "extract_depth": "basic",  # or "advanced"
            "include_images": False
        }
    )
    return response.json()

# Extract article content
content = tavily_extract("https://example.com/article")
print(content["results"][0]["raw_content"])
```

## Response Format

```json
{
  "query": "search query",
  "answer": "AI-generated summary",
  "results": [
    {
      "title": "Page Title",
      "url": "https://example.com",
      "content": "Snippet...",
      "score": 0.95,
      "raw_content": "Full content..."
    }
  ]
}
```

## Best Practices

1. **Use specific queries** - More specific = better results
2. **Check answer field** - Often contains synthesized answer
3. **Verify sources** - Always check result URLs
4. **Rate limits** - Free tier: 1000 requests/month
5. **Advanced depth** - Use for complex research

## Common Use Cases

**Latest News**
```python
result = tavily_search("latest tech news today", max_results=10)
```

**Research**
```python
result = tavily_advanced_search(
    "transformer architecture explained",
    domains=["arxiv.org", "huggingface.co", "pytorch.org"]
)
```

**Fact Check**
```python
result = tavily_search("is claim X true?", search_depth="advanced")
```

---

*Powered by Tavily AI Search API*
