---
name: mcp-playwright
description: Playwright MCP 浏览器自动化控制，基于微软Model Context Protocol，让AI直接操控真实浏览器。支持网页导航、截图、元素交互、表单填写、多标签管理。使用当：需要AI控制真实浏览器、网页自动化测试、MCP协议接入。
---

# Playwright MCP - Model Context Protocol 浏览器控制

## Overview

Playwright MCP 是微软推出的基于 Model Context Protocol (MCP) 的浏览器自动化服务器，让AI可以直接操控真实浏览器，支持：
- 无障碍快照交互
- 网页截图与导航
- 表单填写与点击
- 多标签页管理

本技能提供 Playwright MCP 在 OpenClaw 中的集成使用指南，包含安装配置、常用命令、交互范例。

## Core Capabilities

### 1. 网页导航
- 打开指定 URL
- 后退/前进导航
- 刷新页面
- 获取页面内容快照

### 2. 元素交互
- 点击元素
- 输入文本
- 拖拽操作
- 选择下拉选项

### 3. 视觉输出
- 完整页面截图
- 元素截图
- 可访问性树生成

### 4. 标签管理
- 新建标签页
- 切换标签
- 关闭标签

## Installation 安装

### Prerequisites 前置要求
- Node.js 18+ 已安装
- OpenClaw 已安装
- MCP 客户端配置

### Install command
```bash
# Install Playwright MCP via npm
npm install -g @playwright/mcp

# Install browsers
npx playwright install
```

### Verify installation
```bash
npx @playwright/mcp --version
```

## Connection to OpenClaw 连接 OpenClaw

OpenClaw 通过 MCP 客户端连接到 Playwright MCP 服务器：

1. 配置 MCP 服务器在 `mcp.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp"]
    }
  }
}
```

2. 重启 OpenClaw MCP 客户端加载配置

3. 测试连接：调用 MCP 列表工具验证

## Common Workflows

### Basic browsing workflow
1. `navigate` - 打开目标URL
2. `snapshot` - 获取页面可访问性树
3. 分析页面元素，识别目标
4. `click` / `type` - 执行交互
5. `screenshot` - 获取结果截图

### Form filling workflow
1. 导航到表单页面
2. 获取快照分析字段
3. 逐个字段填充内容
4. 点击提交按钮
5. 验证提交结果

## Examples

### Example: Open Google and search
```
1. navigate: https://www.google.com
2. snapshot -> find search input by role "searchbox"
3. type: "Playwright MCP" into search input
4. click: "Google Search" button
5. screenshot -> show results
```

### Example: Take full page screenshot
```
1. navigate: target-url
2. screenshot: fullPage=true
3. save to output path
```

## References

- [MCP_SPEC.md](references/mcp-spec.md) - Model Context Protocol 协议简介
- [PLAYWRIGHT_MCP_DOCS.md](references/playwright-mcp-docs.md) - Playwright MCP 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - 配置示例
