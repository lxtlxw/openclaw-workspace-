---
name: mcp-trendradar
description: TrendRadar MCP AI舆情监控，全网热点聚合，聚合知乎、微博等11+平台热点话题，AI情感分析，趋势预测追踪，多渠道智能推送。使用当：需要监控全网热点、舆情分析、获取热门话题、趋势预测。
---

# TrendRadar MCP - AI 舆情热点监控

## Overview

TrendRadar MCP 提供全网热点聚合舆情监控能力：
- 聚合 11+ 平台热点（知乎、微博、抖音、B站等）
- AI 情感分析，识别舆论倾向
- 趋势预测追踪，监控热点发展
- 多渠道智能推送热点信息

本技能提供 TrendRadar MCP 在 OpenClaw 中的集成使用指南。

## Core Capabilities

### 1. 热点聚合
- 多平台热点聚合
- 支持知乎、微博、抖音、B站、小红书等主流平台
- 按热度排序展示

### 2. 舆情分析
- AI 情感分析
- 识别舆论正负向倾向
- 舆情概览总结

### 3. 趋势追踪
- 热点话题发展趋势追踪
- 热度变化预测
- 关键词热度监控

### 4. 智能推送
- 按关键词订阅
- 新热点自动推送

## Installation 安装

### Install command
```bash
npm install -g trendradar-mcp
```

### Verify installation
```bash
npx trendradar-mcp --version
```

## Connection to OpenClaw 连接配置

在 OpenClaw MCP 配置文件 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "trendradar": {
      "command": "npx",
      "args": ["trendradar-mcp"],
      "env": {
        "TREND_RADAR_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

获取 API key：[TODO: 填写官方获取地址]

重启 OpenClaw MCP 客户端加载配置。

## Available Tools

### `get_hot_trends`
Get current hot trends from all platforms.
Parameters:
```json
{
  "platform": "string (optional, filter by platform)",
  "limit": "number (optional, default: 20)"
}
```
Returns: List of hot topics with热度 data.

### `analyze_sentiment`
Analyze sentiment for a specific topic.
Parameters:
```json
{
  "keyword": "string"
}
```
Returns: Sentiment analysis result (positive/negative/neutral ratio).

### `track_topic`
Track a topic's trend over time.
Parameters:
```json
{
  "keyword": "string",
  "days": "number (optional, default: 7)"
}
```
Returns: Trend data with热度 changes.

## Common Workflows

### Get today's top hot topics
1. 调用 `get_hot_trends` 获取全网热点
2. 整理按热度排序返回给用户
3. 可选：对热点关键词做情感分析

### Monitor a keyword
1. 用户指定要监控的关键词
2. 调用 `track_topic` 获取趋势数据
3. 返回热度变化图表数据和分析

## Key Features

✅ **11+ 平台聚合** - 覆盖知乎、微博、抖音、B站、小红书等主流内容平台  
✅ **AI 情感分析** - 自动识别舆论情感倾向  
✅ **趋势预测追踪** - 监控话题热度发展变化  
✅ **GitHub 48.8K ⭐** - 开源热门项目，活跃维护  

## Supported Platforms

- 知乎
- 微博
- 抖音
- B站
- 小红书
- 还有 6+ more platforms

## Examples

### Example: Get top 10 hot topics
```
Tool: get_hot_trends(limit=10)
Output: Top 10 hot topics from across platforms with heat scores
```

### Example: Analyze sentiment for a keyword
```
Tool: analyze_sentiment(keyword="人工智能")
Output: Sentiment distribution: positive 65%, neutral 25%, negative 10%
```

## References

- [TREND_RADAR_DOCS.md](references/trendradar-docs.md) - TrendRadar 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - MCP 配置示例

