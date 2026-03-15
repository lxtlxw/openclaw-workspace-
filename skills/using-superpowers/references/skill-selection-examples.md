# Skill Selection Examples - 技能选择示例库

本文件记录常见用户需求对应的技能选择方案，供匹配参考。

---

## 用户需求类型 → 匹配技能

### 文件处理
| 用户需求 | 匹配技能 | 说明 |
|---------|---------|------|
| 编辑PDF文件 | `nano-pdf` | 自然语言编辑PDF |
| 阅读PDF内容 | `pdf` | 分析PDF文档 |
| 处理飞书文档 | `feishu-doc` | 飞书云文档读写 |
| 管理飞书文件 | `feishu-drive` | 飞书云盘文件管理 |

### 搜索信息
| 用户需求 | 匹配技能 | 说明 |
|---------|---------|------|
| 搜索实时信息/新闻 | `tavily-search` | Tavily AI实时全网搜索 |
| 一般网页搜索 | `web_search` | Brave搜索 |
| 提取网页内容 | `web_fetch` / `agent-browser` | 提取可读内容 |
| 天气查询 | `weather` | 获取天气和预报 |

### 开发编码
| 用户需求 | 匹配技能 | 说明 |
|---------|---------|------|
| GitHub操作 | `github` | gh CLI 交互 |
| 创建新技能 | `skill-creator` | 技能创建编辑 |
| 安装新技能 | `skill-vetter` → 安装 | 先安全审计再安装 |
| 浏览器自动化 | `agent-browser` | 网页交互、点击、填表 |

### 系统管理
| 用户需求 | 匹配技能 | 说明 |
|---------|---------|------|
| 安全审计/加固 | `healthcheck` | 主机安全检查配置 |
| 定时任务 | `proactive-agent` | 定期检查、监控变化 |
| 自我改进 | `self-improving-agent` | 持续学习优化 |

### 内容处理
| 用户需求 | 匹配技能 | 说明 |
|---------|---------|------|
| 总结网页/PDF/视频 | `summarize` | 内容总结提取 |
| 安全审计技能 | `skill-vetter` | 检查红flag和风险 |
| 查找技能 | `find-skills` | 搜索可用技能 |

---

## 多技能组合示例

### 示例1："搜索最新的React 18文档，总结重点保存为PDF"
1. `tavily-search` → 搜索最新React 18文档
2. `web_fetch` → 提取文档内容
3. `summarize` → 总结重点内容
4. `nano-pdf` → 将总结生成PDF文件

### 示例2："帮我在飞书知识库创建一篇关于项目计划的文档"
1. `feishu-wiki` → 获取知识库空间信息
2. `feishu-wiki` → 创建新文档节点
3. `feishu-doc` → 写入项目计划内容

### 示例3："检查一下当前主机的安全配置"
1. `healthcheck` → 执行安全审计扫描
2. `summarize` → 总结发现的问题
3. 输出修复建议清单

---

## 决策经验

1. **凡是涉及飞书** → 优先使用飞书系列技能（feishu-doc/feishu-wiki/feishu-drive），不使用通用工具
2. **凡是需要实时信息** → 优先使用`tavily-search`，信息最新最全
3. **凡是需要浏览器交互** → 使用`agent-browser`，不尝试用API模拟浏览器行为
4. **凡是创建新东西** → 检查是否已有技能，没有就用`skill-creator`创建
