# Skill 创建规范指南

## 什么是 Skill

Skill 是 AI CLI 工具（如 Claude Code、OpenClaw）的**可插拔能力模块**。
每个 Skill 是一个文件夹，包含一个 `SKILL.md` 入口文件和相关资源。

AI 读取 `SKILL.md` 后就知道：这个 Skill 能做什么、怎么触发、用什么工具。

## 目录结构规范

```
skill-name/                    # 文件夹名 = skill 标识
├── SKILL.md                   # 入口文件（必须）
├── assets/                    # 运行时数据（可选）
│   ├── profile.md             #   持久化数据
│   └── ...
├── references/                # 参考文档（可选）
│   ├── prompts/               #   Prompt 模板
│   └── guides/                #   使用指南
└── tools/                     # 脚本工具（可选）
    └── *.py                   #   仅 Python，零外部依赖
```

## SKILL.md 规范

### Frontmatter（YAML 头部）

```yaml
---
name: skill-name               # 英文标识，kebab-case
description: "一句话描述"       # 显示在 skill 列表中，要精准触发
argument-hint: "[参数提示]"     # 可选，提示用户传什么参数
version: "1.0.0"               # 语义化版本
user-invocable: true            # 用户可以直接 /skill-name 调用
allowed-tools: Read, Write, Edit, Bash  # 允许使用的工具
---
```

### Body（正文）

正文是给 AI 看的指令，包含：
1. **触发条件** — 什么情况下激活这个 Skill
2. **工具使用规则** — 用什么工具做什么事
3. **主流程** — 一步步怎么执行
4. **输出格式** — 输出长什么样
5. **特殊规则** — 边界情况处理

### 关键规则

| 规则 | 说明 |
|------|------|
| `<this-skill-dir>` | 引用本 Skill 内的文件用这个占位符 |
| 不硬编码路径 | 禁止 `/Users/xxx/`、`~/.claude/skills/` |
| 不用 shell 脚本 | 脚本只用 Python（跨平台） |
| 正文 < 500 行 | 超了就拆到 references/ |
| 零外部依赖 | pip install 都不要，用 stdlib |

## 生成 Skill 的 Checklist

创建一个新 Skill 前，检查以下清单：

### 必须有 ✅
- [ ] `SKILL.md` 存在且有完整 frontmatter
- [ ] `name` 是 kebab-case 英文
- [ ] `description` 一句话，中英双语
- [ ] `user-invocable: true`（用户可调用）
- [ ] 触发条件写清楚了
- [ ] 主流程有具体步骤
- [ ] 引用文件用 `<this-skill-dir>/` 前缀

### 应该有 ⭐
- [ ] 输出格式有示例
- [ ] 错误处理有说明
- [ ] 版本号
- [ ] argument-hint（如果有子命令）

### 加分项 ✨
- [ ] references/setup.md（安装说明）
- [ ] references/guides/（使用指南）
- [ ] 多语言支持（中英）
