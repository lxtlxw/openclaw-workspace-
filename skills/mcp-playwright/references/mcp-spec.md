# Model Context Protocol (MCP) 简介

## What is MCP

Model Context Protocol (MCP) 是一个开放协议，让AI模型可以安全地连接到外部工具和数据源，实现：
- AI → 外部工具调用
- 工具 → AI 上下文返回
- 标准化的能力暴露接口

## Core Concepts

### Server
暴露一组能力（工具、资源、提示词）给客户端。Playwright MCP 就是一个 MCP Server，提供浏览器控制能力。

### Client
连接到一个或多个 Server，调用 Server 暴露的能力，整合结果返回给AI。OpenClaw 作为 MCP Client 连接 Playwright MCP。

### Tools
可调用函数，每个工具有名称、描述、输入Schema。Playwright MCP 提供这些工具：
- `navigate` - 导航到URL
- `click` - 点击元素
- `type` - 输入文本
- `screenshot` - 截图
- `snapshot` - 获取可访问性快照
- `close` - 关闭页面
- `goBack` - 后退
- `goForward` - 前进
- `reload` - 刷新
- `newTab` - 新建标签
- `switchTab` - 切换标签
- `closeTab` - 关闭标签

## Resources

Official website: https://modelcontextprotocol.io/
GitHub: https://github.com/modelcontextprotocol
