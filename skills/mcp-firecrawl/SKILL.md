---
name: mcp-firecrawl
description: Firecrawl MCP 网页爬取工具，零代码爬取网页，自动转换为结构化 Markdown 数据，智能绕过反爬，支持批量抓取。使用当：需要爬取网页内容、提取网页结构化数据、批量站点抓取。
---

# Firecrawl MCP - 网页爬取结构化提取

## Overview

Firecrawl MCP 是基于 Model Context Protocol 的网页爬取服务，能够：
- 智能绕过反爬机制
- 将任意网页爬取转换为干净的 Markdown
- 提取结构化数据
- 支持批量站点抓取

本技能提供 Firecrawl MCP 在 OpenClaw 中的集成使用指南。

## Core Capabilities

### 1. 网页爬取
- 单个 URL 爬取
- 自动处理反爬
- 返回干净 Markdown 格式内容

### 2. 批量爬取
- 多个 URL 批量抓取
- 统一输出格式

### 3. 结构化输出
- 自动清理 HTML 杂质
- Markdown 格式输出
- 支持提取元数据

## Installation 安装

### Prerequisites
- Node.js 18+
- Firecrawl API key (get from https://firecrawl.dev/)

### Install command
```bash
npm install -g @mendableai/mcp-server-firecrawl
```

### Verify installation
```bash
npx @mendableai/mcp-server-firecrawl --version
```

## Connection to OpenClaw 连接配置

在 OpenClaw MCP 配置文件 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["@mendableai/mcp-server-firecrawl"],
      "env": {
        "FIRECRAWL_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

替换 `your-api-key-here` 为你的 Firecrawl API key。重启 OpenClaw MCP 客户端加载配置。

## Available Tools

### `crawl_url`
Crawl a single URL and get Markdown content.
Parameters:
```json
{
  "url": "string",
  "extract_metadata": "boolean (optional, default: true)"
}
```
Returns: Markdown content + metadata.

### `crawl_sitemap`
Crawl all URLs in a sitemap (bulk crawling).
Parameters:
```json
{
  "sitemap_url": "string",
  "limit": "number (optional, default: 100)"
}
```
Returns: Array of crawled results with Markdown content.

## Common Workflows

### Single page crawl
1. 准备目标 URL
2. 调用 `crawl_url` 工具
3. 获取 Markdown 结果
4. 根据需求进一步处理（总结、分析、保存）

### Bulk site crawl
1. 获取站点 sitemap URL
2. 调用 `crawl_sitemap` 工具设置 limit
3. 批量获取所有页面内容
4. 整合导出

## Key Features

✅ **智能绕过反爬** - Firecrawl 处理反爬机制，不需要你处理  
✅ **零代码配置** - 只需 API key，直接使用  
✅**干净输出** - 自动去除广告、导航、杂质，只保留核心内容，输出标准 Markdown  
✅ **结构化提取** - 自动提取标题、描述、链接等元数据  
✅ **批量抓取** - 通过 sitemap 批量抓取整站

## Examples

### Example: Crawl a blog post
```
Input: https://example.com/blog/post
Tool: crawl_url(url="https://example.com/blog/post")
Output: Clean Markdown content of the blog post
```

### Example: Bulk crawl documentation
```
Input: https://example.com/sitemap.xml
Tool: crawl_sitemap(sitemap_url="https://example.com/sitemap.xml", limit=50)
Output: 50 pages of documentation in Markdown
```

## References

- [FIRECRAWL_DOCS.md](references/firecrawl-docs.md) - Firecrawl 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - MCP 配置示例

