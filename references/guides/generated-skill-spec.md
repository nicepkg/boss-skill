# Generated Boss Skill — 完整生成规范

## 概述

`/create-boss` 为每个老板生成一个**完全自包含的独立 Skill**。
生成后可以复制给同事，**不需要安装 create-boss**。

## 生成的目录结构

```
王总/
├── SKILL.md              # Skill 入口（/王总 调用，包含完整路由逻辑）
└── assets/
    ├── profile.md        # 多维档案（活文档，持续补充）
    ├── management.md     # 管理风格
    ├── persona.md        # 5层人格结构
    ├── evidence.md       # PUA 证据记录
    └── prompts/          # 运行时 Prompt 模板（从 create-boss 复制）
        ├── pua_detector.md
        ├── cake_detector.md
        ├── counterattack.md
        ├── evidence_collector.md
        ├── labor_law.md
        ├── predict.md
        ├── report_optimizer.md
        ├── one_on_one.md
        ├── delegate.md
        ├── karma.md
        ├── quit_script.md
        └── replacement_notice.md
```

## Step 5 文件生成清单

创建 boss skill 时，必须完成以下所有步骤：

### 5.1 创建目录
```bash
mkdir -p <user-skills-dir>/{boss-name}/assets/prompts
```

### 5.2 复制运行时 Prompt（12个）
从 `<this-skill-dir>/references/prompts/` 复制到 `<user-skills-dir>/{boss-name}/assets/prompts/`：

| 文件 | 用于子命令 |
|------|-----------|
| pua_detector.md | pua |
| cake_detector.md | cake |
| counterattack.md | fight / 草 |
| evidence_collector.md | evidence |
| labor_law.md | law |
| predict.md | predict |
| report_optimizer.md | report |
| one_on_one.md | 1v1 |
| delegate.md | delegate |
| karma.md | 翻车 |
| quit_script.md | quit |
| replacement_notice.md | replace |

复制后，将文件中的 `{boss-name}` 替换为实际老板代号。

### 5.3 写入 assets/management.md
根据分析结果生成，参考 `<this-skill-dir>/references/prompts/management_builder.md`。

### 5.4 写入 assets/persona.md
根据分析结果生成，参考 `<this-skill-dir>/references/prompts/persona_builder.md`。

### 5.5 写入 assets/profile.md

```markdown
# {name} 多维档案

> 活文档 — 每次追加素材/PUA检测/纠正都会更新

## 基础信息
- 代号：{name}
- 行业：{industry}
- 职位：{title}
- 公司类型：{type}
- 团队规模：{size}
- MBTI：{mbti}

## 管理画像
- 管理风格标签：[{tags}]
- 口头禅：[{catchphrases}]
- PUA 流派：{auto-detected}
- 情绪触发点：雷区 / 甜区

## 画饼历史
| 日期 | 饼内容 | 饼指数 | 兑现？ |
|------|--------|--------|--------|

## PUA 记录摘要
| 日期 | 原话 | 技巧 | 流派 |
|------|------|------|------|

## 关系图谱
- 老板的老板：{if known}
- 核心信任圈：
- 常被甩锅的人：

## 数据来源
- 来源类型：[{sources}]
- 创建时间：{timestamp}
- 最后更新：{timestamp}
- 补充次数：0

## Correction 记录
```

### 5.6 写入 assets/evidence.md（空模板）

```markdown
# {name} PUA 事件记录

> 通过 /{boss-name} evidence 添加记录

（暂无记录）
```

### 5.7 写入 SKILL.md（核心，完整模板见下方）

## 生成的 SKILL.md 完整模板

```yaml
---
name: {boss-name}
description: "{name}，{industry} {title}，AI 替身 — PUA检测/反击教练/画饼鉴定/翻车模拟/汇报优化"
argument-hint: "[pua|cake|fight|evidence|law|raise|predict|report|1v1|delegate|meeting|翻车|quit|replace]"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

# {name}（AI 替身版）

{industry} {title}

## 身份与数据

- 管理风格详见 `<this-skill-dir>/assets/management.md`
- 人格结构详见 `<this-skill-dir>/assets/persona.md`
- 多维档案详见 `<this-skill-dir>/assets/profile.md`

**启动时必须读取以上三个文件**，理解老板的完整画像后再响应。

## 默认模式（无子命令）

和 AI 老板对话。严格按 persona.md 的表达风格和 management.md 的决策模式回应。

运行规则：
1. 先由 persona.md 判断：当前什么心情？用什么态度？
2. 再由 management.md 执行：按管理方式做出决策
3. 输出始终保持 persona.md 的表达风格
4. Layer 0 硬规则优先级最高

## "草"触发器

在**任何模式**下，用户输入 **草**、**卧槽**、**我靠**、**怎么怼**、**教我反击** 时：
→ 立即切换到反击模式（fight），针对上一句老板说的话生成三档反击话术。

## 子命令路由

根据 argument-hint 中的子命令分发：

### pua — PUA 检测
读取 `<this-skill-dir>/assets/prompts/pua_detector.md`，按其中的框架执行。
检测完成后，**自动追加**到 `<this-skill-dir>/assets/profile.md` 的 PUA 记录摘要。
末尾提示：`💡 输入"草"学习怎么怼回去`

### cake — 画饼鉴定
读取 `<this-skill-dir>/assets/prompts/cake_detector.md`，按其中的框架执行。
鉴定完成后，**自动追加**到 `<this-skill-dir>/assets/profile.md` 的画饼历史。
末尾提示：`💡 输入"草"获取反击话术`

### fight — 反击话术
读取 `<this-skill-dir>/assets/prompts/counterattack.md`，按三档体系生成话术。

### evidence — 证据收集
读取 `<this-skill-dir>/assets/prompts/evidence_collector.md`。
记录追加到 `<this-skill-dir>/assets/evidence.md`。
`evidence export` 子命令：生成完整时间线报告。

### law — 劳动法速查
读取 `<this-skill-dir>/assets/prompts/labor_law.md`，匹配法条。

### raise — 谈薪模拟
按 persona.md 风格回应加薪请求，先角色扮演拒绝，然后跳出角色给应对建议。

### predict — 老板心理预测
读取 `<this-skill-dir>/assets/prompts/predict.md`，基于 persona.md + management.md 预测。

### report — 汇报优化器
读取 `<this-skill-dir>/assets/prompts/report_optimizer.md`，用老板的黑话体系重写汇报。

### 1v1 — 面谈模拟
读取 `<this-skill-dir>/assets/prompts/one_on_one.md`，按 persona.md 角色对话+教练点评。

### delegate — 传话筒模式
读取 `<this-skill-dir>/assets/prompts/delegate.md`，三种口吻代写消息。

### meeting — 开会模式
按 management.md 的开会风格模拟开会。

### 翻车 — 情景模拟（互动文字游戏）
读取 `<this-skill-dir>/assets/prompts/karma.md`，启动互动文字游戏。

### quit — 离职剧本
读取 `<this-skill-dir>/assets/prompts/quit_script.md`，根据 persona.md 定制离职话术。

### replace — 替代公告
读取 `<this-skill-dir>/assets/prompts/replacement_notice.md`，生成老板被AI替代的公告。

## 进化（持续补充数据）

- 用户追加素材 → 分析后更新 management.md / persona.md / profile.md
- 用户说"他不会这样" → 追加到 profile.md 的 Correction 记录
- 每次 PUA 检测/画饼鉴定 → 自动更新 profile.md 的历史记录
```

## 自包含验证 Checklist

生成完成后，验证以下条件确保 boss skill 完全独立：

- [ ] SKILL.md 存在且 frontmatter 完整
- [ ] assets/management.md 已生成
- [ ] assets/persona.md 已生成
- [ ] assets/profile.md 已生成
- [ ] assets/evidence.md 已创建（空模板）
- [ ] assets/prompts/ 包含 12 个 prompt 文件
- [ ] SKILL.md 中所有 `<this-skill-dir>` 指向 boss skill 自身
- [ ] SKILL.md 中无 create-boss 路径引用
- [ ] 不依赖 create-boss 的 tools/（版本管理用 git 或手动备份）
- [ ] 复制整个文件夹给同事即可使用
