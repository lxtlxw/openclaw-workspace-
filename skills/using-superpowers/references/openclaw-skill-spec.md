# OpenClaw Skill Specification

## 技能结构规范

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML frontmatter (必需) - name 和 description
│   └── Markdown 操作指南 (必需)
├── scripts/ (可选) - 可执行脚本
├── references/ (可选) - 参考文档
└── assets/ (可选) - 模板/资源文件
```

## YAML Frontmatter 要求

```yaml
---
name: skill-name
description: 清晰描述技能做什么，什么时候使用这个技能。一定要包含触发场景。
---
```

- **name**: 小写字母+连字符，不允许空格和大写
- **description**: 必须包含"做什么"和"什么时候用"，这是技能匹配的关键

## SKILL.md 写作原则

1. **简洁优先** → 只保留AI真正需要的信息，减少token浪费
2. **渐进式披露** → 核心流程放SKILL.md，详细参考放references/
3. **命令式语气** → 使用"做XXX"、"运行XXX"，不使用解释性冗余文字
4. **结构化** → 使用标题层级，清晰导航

## 技能触发原则

技能的description字段决定了什么时候这个技能会被选中：
- 描述清楚具体任务类型，比如"处理PDF文件，编辑PDF，旋转PDF，提取文本"
- 描述清楚触发关键词，比如"使用当：用户需要处理PDF文件"

## 参考链接
- 官方文档：https://docs.openclaw.ai/skills
- GitHub源码：https://github.com/openclaw/openclaw
