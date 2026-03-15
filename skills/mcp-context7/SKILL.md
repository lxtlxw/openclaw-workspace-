---
name: mcp-context7
description: Context7 MCP 实时开发文档，提供 9000+ 开发库最新文档，实时版本同步，向量语义搜索，精准代码示例。告别过时代码建议，AI编码时提供最新准确文档。使用当：AI编码需要查询最新库文档、获取代码示例、查找API用法。
---

# Context7 MCP - 实时开发文档搜索

## Overview

Context7 MCP 为AI编码提供**最新实时开发文档**，解决AI训练数据过时问题：
- 9000+ 开发库文档覆盖
- 实时版本同步，始终获取最新版本文档
- 向量语义搜索，精准匹配需求
- 提供可运行代码示例
- 每周 514K+ 下载，广泛使用

本技能提供 Context7 MCP 在 OpenClaw 中的集成使用指南。

## Core Capabilities

### 1. 库文档搜索
- 语义搜索 9000+ 开发库文档
- 自动匹配当前最新版本
- 返回官方文档摘要+代码示例

### 2. 版本感知
- 支持指定版本查询
- 自动同步库的最新版本更新
- 避免训练数据过时导致错误建议

### 3. 精准代码示例
- 提取官方文档中的真实代码示例
- 直接可用，减少调试时间

## Installation 安装

### Install command
```bash
npm install -g @upstash/context7-mcp
```

### Verify installation
```bash
npx @upstash/context7-mcp --version
```

## Connection to OpenClaw 连接配置

在 OpenClaw MCP 配置文件 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@upstash/context7-mcp"]
    }
  }
}
```

无需 API key，可直接使用。重启 OpenClaw MCP 客户端加载配置。

## Available Tools

### `get_library_docs`
Get documentation for a software library.
Parameters:
```json
{
  "libraryName": "string",
  "version": "string (optional, defaults to latest)",
  "query": "string (optional, semantic search query)"
}
```
Returns: Documentation content with code examples.

## Common Workflows

### Coding with up-to-date docs
1. 用户提问关于某个库的用法
2. 调用 `get_library_docs` 获取最新文档
3. 基于最新文档回答用户问题，给出正确代码示例
4. 如果有多个版本，可以指定版本查询

### Debugging outdated code
1. 代码报错怀疑是版本过时
2. 查询当前最新版本的文档
3. 对比发现API变更，给出更新后的正确代码

## Key Features

✅ **9000+ 库覆盖** - 覆盖绝大多数 npm/pypi 热门开发库  
✅ **实时版本同步** - 始终获取最新文档，告别过时建议  
✅ **向量语义搜索** - 智能匹配你要找的内容  
✅ **精准代码示例** - 直接来自官方文档的可运行示例  
✅ **无需 API key** - 免费可用，直接使用  

## Statistics

- Weekly downloads: **514K+**
- Total libraries: **9000+**

## Examples

### Example: Get React 18 documentation
```
Tool: get_library_docs(
  libraryName="react",
  version="18",
  query="hooks usage"
)
Output: Latest React 18 hooks documentation with examples
```

### Example: Get latest FastAPI docs
```
Tool: get_library_docs(
  libraryName="fastapi",
  query="dependency injection"
)
Output: Latest FastAPI dependency injection docs
```

## References

- [CONTEXT7_DOCS.md](references/context7-docs.md) - Context7 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - MCP 配置示例

