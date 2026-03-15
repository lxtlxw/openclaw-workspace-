---
name: using-superpowers
description: 技能架构师超级能力，自动识别用户需求，选择匹配技能，组合多个技能完成复杂任务，让AI充分发挥所有OpenClaw技能的能力。激活当：需要处理复杂任务、组合多个技能能力、自动选择正确技能完成用户需求。
---

# Using Superpowers - 技能架构师超级能力

## Overview

本技能赋予AI技能架构师能力，能够：
1. 深度分析用户真实需求
2. 从所有可用技能中自动选择最匹配的一个或多个技能
3. 按照各技能的规范正确调用技能完成子任务
4. 有序组合多个技能，分步执行复杂任务
5. 整合各技能输出，给用户完整的结果

## Core Workflow - 核心工作流

### Step 1: 需求分解
- 通读用户完整对话，理解真实需求，拆解为可执行子任务
- 识别每个子任务需要什么类型的能力

### Step 2: 技能匹配
- 遍历可用技能列表（通过 `find-skills` 搜索）
- 根据技能描述匹配最适合当前子任务的技能
- 优先选择专门技能，不使用通用能力解决专业问题
- 如果多个技能都适用，按优先级组合使用

### Step 3: 加载技能知识
- 对选中的每个技能，读取其 `SKILL.md`
- 理解技能的使用方法、触发条件、调用流程
- 按照技能指导准备执行

### Step 4: 分步执行
- 按依赖关系排序子任务，先执行前置任务
- 每个子任务严格遵循对应技能的操作流程
- 记录每一步结果，用于后续步骤

### Step 5: 结果整合
- 将所有子任务结果整合为连贯完整的回答
- 清理中间过程，只给用户最终输出
- 保留必要的说明，帮助用户理解执行过程

## Decision Rules - 决策规则

### When to use multiple skills
- 任务涉及多个不同领域知识
- 需要不同工具能力组合才能完成
- 一个技能的输出是另一个技能的输入

**Example:** 用户要"搜索最新的React文档，总结成PDF"
- 使用 `tavily-search` 搜索最新文档
- 使用 `summarize` 总结内容
- 使用 `nano-pdf` 生成PDF

### When to use skill-creator
- 当前没有匹配的技能能满足需求
- 需求是特定领域的重复性任务
- 创建新技能能大幅提升未来效率

### Priority Rules
1. **Workspace技能优先** → `~/.openclaw/workspace/skills/` 中的技能覆盖全局技能
2. **专门技能优先** → 不要用通用技能替代专门技能，比如用 `feishu-doc` 处理飞书文档，不用通用文档处理
3. **已安装技能优先** → 优先使用已掌握的技能，不重新发明轮子

## Tools You'll Use

### find-skills
- 搜索可用技能：`find-skills` 技能可以按关键词搜索技能
- Usage: 调用 `find-skills` 搜索关键词，找到匹配技能

### memory_search
- 搜索已学习的技能知识和使用经验
- 复用之前成功的技能组合方案

## Examples

### Example 1: 用户需求"帮我创建一个处理PDF的新技能"
1. 识别需求 → 创建新技能 → 匹配 `skill-creator`
2. 调用 `skill-creator` 按流程创建新技能
3. 验证打包 → 完成交付

### Example 2: 用户需求"搜索今天北京天气，然后提醒我带伞"
1. 分解需求：获取天气 → 判断是否需要带伞 → 提醒
2. 技能匹配：`weather` 获取天气，`proactive-agent` 设置提醒
3. 先调用 `weather` 获取天气预报
4. 根据降雨概率判断是否需要提醒
5. 需要提醒则调用 `proactive-agent` 设置定时提醒

## References

- [OPENCLAW_SKILL_SPEC.md](references/openclaw-skill-spec.md) - OpenClaw技能规范参考
- [SKILL_SELECTION_EXAMPLES.md](references/skill-selection-examples.md) - 技能选择示例库
