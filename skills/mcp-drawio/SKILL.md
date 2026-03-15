---
name: mcp-drawio
description: Draw.io MCP 官方出品，AI一句话生成架构图，支持XML图表生成、Mermaid语法转换、CSV转流程图、聊天内联预览。使用当：需要AI生成架构图、流程图、系统架构图、从描述自动生成图表。
---

# Draw.io MCP - AI 一句话画架构图

## Overview

Draw.io MCP 是官方出品的 AI 图表生成工具，一句话描述自动生成架构图：
- AI 自然语言描述 → 自动生成 Draw.io 图表
- 支持架构图、流程图、各种技术图表
- 多种格式转换输出

本技能提供 Draw.io MCP 在 OpenClaw 中的集成使用指南。

## Core Capabilities

### 1. AI 图表生成
- 自然语言描述需求，AI自动生成架构图
- 支持系统架构图、流程图、ER图等各种图表类型

### 2. 格式转换
- XML图表生成 → Draw.io 原生格式
- Mermaid 语法转换 → Mermaid → Draw.io 格式
- CSV 转流程图 → CSV数据 → 自动生成流程图

### 3. 内联预览
- 聊天内直接预览生成的图表
- 快速迭代调整图表

## Installation 安装

### Install command
```bash
npm install -g @drawio/mcp-server
```

### Verify installation
```bash
npx @drawio/mcp-server --version
```

## Connection to OpenClaw 连接配置

在 OpenClaw MCP 配置文件 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": ["@drawio/mcp-server"]
    }
  }
}
```

无需额外 API key，直接使用。重启 OpenClaw MCP 客户端加载配置。

## Available Tools

### `generate_diagram`
Generate diagram from natural language description.
Parameters:
```json
{
  "description": "string",
  "type": "string (architecture|flowchart|er|custom)"
}
```
Returns: Draw.io XML diagram + preview.

### `convert_mermaid`
Convert Mermaid syntax to Draw.io diagram.
Parameters:
```json
{
  "mermaid_code": "string"
}
```
Returns: Draw.io diagram.

### `csv_to_flowchart`
Convert CSV data to flowchart.
Parameters:
```json
{
  "csv_data": "string"
}
```
Returns: Flowchart diagram.

## Common Workflows

### Generate system architecture diagram
1. User describes system architecture in natural language
2. Call `generate_diagram` with description and type "architecture"
3. Get generated diagram with preview
4. User can request adjustments, AI regenerates

### Convert Mermaid to editable Draw.io
1. Have Mermaid code
2. Call `convert_mermaid`
3. Get editable Draw.io diagram

## Key Features

✅ **官方出品** - Draw.io 官方开发维护  
✅ **AI一句话生成** - 自然语言描述 → 架构图  
✅ **多种格式支持** - XML/Mermaid/CSV → Draw.io  
✅ **聊天内联预览** - 直接在聊天中预览结果  
✅ **17.2K weekly downloads** - 广泛使用  

## Statistics

- Weekly downloads: **17.2K+**
- Official project by Draw.io

## Examples

### Example: Generate microservices architecture
```
User: "Generate a microservices architecture with API gateway, auth service, product service, order service, and database per service"
Tool: generate_diagram(
  description="Generate a microservices architecture with API gateway, auth service, product service, order service, and database per service",
  type="architecture"
)
Output: Draw.io architecture diagram with preview
```

## References

- [DRAWIO_MCP_DOCS.md](references/drawio-mcp-docs.md) - Draw.io MCP 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - MCP 配置示例

