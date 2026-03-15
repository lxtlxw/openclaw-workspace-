---
name: mcp-n8n
description: n8n MCP Server 工作流自动化，AI一句话编排自动化工作流，支持 500+ 集成节点，工作流创建/监控/管理全流程。使用当：需要AI自动化工作流、创建n8n工作流、监控执行状态、管理自动化凭证。
---

# n8n MCP - AI 工作流自动化编排

## Overview

n8n MCP Server 让AI可以直接操作 n8n 工作流自动化平台：
- AI 一句话描述需求，自动创建完整工作流
- 500+ 预置集成节点，连接各种服务
- 执行状态实时监控
- 凭证安全管理

本技能提供 n8n MCP 在 OpenClaw 中的集成使用指南。

## Core Capabilities

### 1. 工作流管理
- 自动创建新工作流
- 根据自然语言描述编排工作流节点
- 编辑已有工作流

### 2. 执行监控
- 查询工作流执行状态
- 获取执行日志
- 失败告警查看

### 3. 凭证管理
- 安全管理第三方服务凭证
- 创建更新删除凭证

## Installation 安装

### Prerequisites
- 自托管 n8n 实例或 n8n.cloud 账号
- n8n API key

### Install command
```bash
npm install -g n8n-mcp-server
```

### Verify installation
```bash
npx n8n-mcp-server --version
```

## Connection to OpenClaw 连接配置

在 OpenClaw MCP 配置文件 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["n8n-mcp-server"],
      "env": {
        "N8N_HOST": "your-n8n-host",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

配置说明：
- `N8N_HOST`: your n8n host, e.g. `http://localhost:5678` or `https://your-n8n.instance`
- `N8N_API_KEY`: Get from n8n settings → API

重启 OpenClaw MCP 客户端加载配置。

## Available Tools

### `create_workflow`
Create a new workflow from description.
Parameters:
```json
{
  "name": "string",
  "description": "string (natural language description of what the workflow does)"
}
```

### `list_workflows`
List all existing workflows.

### `get_workflow_status`
Get execution status of a workflow.
Parameters:
```json
{
  "workflowId": "string"
}
```

### `execute_workflow`
Trigger execution of a workflow.
Parameters:
```json
{
  "workflowId": "string",
  "data": "object (optional, input data)"
}
```

### `create_credential`
Create a new credential for external service.
Parameters:
```json
{
  "type": "string",
  "data": "object"
}
```

## Common Workflows

### AI auto-create workflow
1. User describes what the automation should do in natural language
2. AI calls `create_workflow` with the description
3. n8n MCP automatically creates the workflow with correct nodes and connections
4. AI can trigger execution with `execute_workflow`

### Monitor existing automation
1. Call `list_workflows` to get all workflows
2. Select the workflow to monitor
3. Call `get_workflow_status` to check latest execution
4. Report status to user

## Key Features

✅ **AI-native workflow creation** - 一句话描述需求，AI自动编排工作流  
✅ **500+ integrations** - 预置 500+ 集成节点，连接各种服务  
✅ **Full lifecycle management** - 创建 → 执行 → 监控 → 编辑全流程  
✅ **Secure credential management** - 安全存储管理第三方凭证  
✅ **Popular open source** - GitHub 72K+ ⭐，活跃开发  

## Examples

### Example: Create daily report workflow
```
User request: "Create a workflow that fetches sales data from Google Sheets every day at 9 AM, sends a summary email to the team"
Tool: create_workflow(
  name="Daily Sales Report",
  description="Fetches sales data from Google Sheets every day at 9 AM, sends a summary email to the team"
)
Output: Created workflow with schedule trigger, Google Sheets node, transform, email node
```

## References

- [N8N_MCP_DOCS.md](references/n8n-mcp-docs.md) - n8n MCP 官方文档整理
- [CONFIG_EXAMPLE.json](references/config-example.json) - MCP 配置示例

