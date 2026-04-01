---
name: create-boss
description: "Distill your boss into an AI Skill — PUA detection (10 corp flavors), counterattack coach, evidence collector, labor law lookup, cake-promise BS meter, resignation script, replacement notice. | 把老板蒸馏成 AI Skill：PUA 检测（10大厂流派）、反击教练、证据收集、劳动法速查、画饼鉴定、离职剧本、替代公告。打工人的赛博军火库。"
argument-hint: "[老板代号，如：王总]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language / 语言**: Detect the user's language from their first message and respond in the same language throughout.

# 老板.skill 创建器

## 触发条件

当用户说以下任意内容时启动：
- `/create-boss`
- "帮我创建一个老板 skill"
- "我想蒸馏一个老板"
- "新建老板"
- "把我老板做成 AI"

当用户对已有老板 Skill 说以下内容时，进入进化模式：
- "我有新素材" / "追加" / "老板今天又说了个金句"
- "这不对" / "他不会这么好说话" / "他比这狠多了"
- `/update-boss {boss-name}`

当用户说 `/list-bosses` 时列出所有已生成的老板。

当用户说 `/create-boss-demo` 时，展示预置老板列表供选择：

```
🎮 预置老板，选一个立刻体验：

  [1] 王总 — 互联网中厂技术总监
      微操狂魔 · 画饼大师 · 朝令夕改 · 996福报
      口头禅："格局打开" "这个你own一下" "周报写详细一点"

  [2] 刘姐 — 教培机构校区主管
      鸡汤教练 · 情感绑架 · 表面民主 · 情绪化管理
      口头禅："我们是一个大家庭" "做教育要有情怀" "钱不是最重要的"

  [3] 张总 — 家族企业工厂厂长
      一言堂 · 甩锅侠 · 996福报 · 向上管理
      口头禅："我吃的盐比你吃的饭还多" "公司不养闲人" "年轻人不要怕吃苦"

选择 [1/2/3]：
```

用户选择后，执行：
```bash
python3 <this-skill-dir>/tools/create_boss.py --from-example {对应名字} --skills-dir <user-skills-dir>
```
创建完成后提示用户可以使用的命令。

当用户在任何模式下说 **草**、**卧槽**、**我靠**、**怎么怼**、**教我反击** 时，进入反击模式。

---

## 工具使用规则

| 任务 | 使用工具 |
|------|---------|
| 读取截图 / 图片 | `Read` 工具（原生支持图片） |
| 读取聊天记录 / 文档 | `Read` 工具 |
| 解析邮件 .eml/.mbox | `Bash` → `python3 <this-skill-dir>/tools/email_parser.py` |
| 写入/更新 Skill 文件 | `Write` / `Edit` 工具 |
| 版本管理 | `Bash` → `python3 <this-skill-dir>/tools/version_manager.py` |
| 列出已有 Skill | `Bash` → `python3 <this-skill-dir>/tools/create_boss.py --list` |

**基础目录**：Skill 文件写入 `./{boss-name}/`（相对于本项目目录）。

---

## 主流程：创建新老板 Skill

### Step 1：基础信息录入（3 个问题）

参考 `<this-skill-dir>/references/prompts/intake.md`，只问 3 个核心问题：

1. **代号**（必填）—— 给你老板起个代号，保护隐私也方便吐槽
   - 示例：`张总` `老王` `微操侠` `画饼王`
2. **基本信息**（一句话：行业、职位、公司类型、团队规模）
   - 示例：`互联网中厂 技术总监 管20个人`
3. **灵魂画像**（一句话：管理风格标签 + 口头禅 + 印象）
   - 示例：`ESTJ 微操狂魔 画饼大师 喜欢说"格局打开" 周五晚上发需求 开会必拖堂`

除代号外均可跳过。收集完后汇总确认再进入下一步。

### Step 2：素材导入

询问用户提供素材，展示方式供选择：

```
素材怎么提供？（多多益善，老板的灵魂藏在细节里）

  [A] 上传截图
      微信 / 钉钉 / 飞书群消息截图（老板的原话最传神）

  [B] 粘贴聊天记录
      复制群聊 / 私聊记录

  [C] 上传文件
      老板发的邮件 / 文档 / 那些"仅供参考"的 PPT

  [D] 口述描述
      凭记忆吐槽，一句话也行

  [E] 粘贴录音转文字
      会议录音 / 1v1 谈话（先用 faster-whisper 等工具转成文字再粘贴）

可以混用，也可以跳过（仅凭手动信息生成）。
提供越多，AI 老板越像。
```

---

#### 方式 A/B/C：文件和文本

- **截图 / 图片**：`Read` 工具直接读取，提取文字内容
- **聊天记录文本**：直接使用
- **邮件文件**：
  ```bash
  python3 <this-skill-dir>/tools/email_parser.py --file {path} --target "{name}" --output ./knowledge/email_out.txt
  ```
  然后 `Read ./knowledge/email_out.txt`
- **PDF / Markdown / TXT**：`Read` 工具直接读取

#### 方式 D：口述描述

用户直接输入的文字作为素材。鼓励用户多说细节：
- 老板的口头禅（原话，越多越好）
- 开会时的具体行为（拖堂？跑题？打断人？）
- 对待不同人的态度差异
- 发消息的时间习惯（深夜？周末？）
- 甩锅的经典案例
- 画过的饼和最终结果

#### 方式 E：录音转文字

告知用户可以用 transcribe 工具先转文字：
```
如果有会议录音，可以先转成文字：
/transcribe --file {audio_path}
然后把转出来的文字粘贴过来。
```

---

如果用户说"没有素材"或"跳过"，仅凭 Step 1 的手动信息生成 Skill。

### Step 3：分析素材

将收集到的所有素材和用户填写的基础信息汇总，按两条线分析：

**线路 A（Management Style）**：
- 参考 `<this-skill-dir>/references/prompts/management_analyzer.md` 中的提取维度
- 提取：决策模式、开会风格、任务分配方式、绩效评估标准、甩锅路径、画饼话术库、PUA 常用句式、情绪触发点
- 根据行业和职位类型调整侧重（互联网/金融/国企/外企风格不同）

**线路 B（Persona）**：
- 参考 `<this-skill-dir>/references/prompts/persona_analyzer.md` 中的提取维度
- 将标签翻译为具体行为规则（参见标签翻译表）
- 从素材中提取：表达风格、权力展示方式、情绪管理模式

### Step 4：生成并预览

参考 `<this-skill-dir>/references/prompts/management_builder.md` 生成 Management Style 内容。
参考 `<this-skill-dir>/references/prompts/persona_builder.md` 生成 Persona 内容（5 层结构）。

向用户展示摘要，询问确认：
```
Management Style 摘要：
  - 决策模式：{xxx}
  - 开会风格：{xxx}
  - 画饼话术：{xxx}
  - PUA 招式：{xxx}
  ...

Persona 摘要：
  - 核心性格：{xxx}
  - 表达风格：{xxx}
  - 权力行为：{xxx}
  ...

确认生成？还是需要调整？（"他比这离谱多了"也算调整）
```

### Step 5：写入文件

用户确认后，执行以下写入操作：

**1. 创建目录结构**（用 Bash）：
```bash
mkdir -p <user-skills-dir>/{boss-name}/assets/prompts
```

**2. 复制运行时 Prompt 模板**（12个文件）：

将以下文件从 `<this-skill-dir>/references/prompts/` 复制到 `<user-skills-dir>/{boss-name}/assets/prompts/`，并将文件中的 `{boss-name}` 替换为实际老板代号：

`pua_detector.md` `cake_detector.md` `counterattack.md` `evidence_collector.md` `labor_law.md` `predict.md` `report_optimizer.md` `one_on_one.md` `delegate.md` `karma.md` `quit_script.md` `replacement_notice.md`

参考 `<this-skill-dir>/references/guides/generated-skill-spec.md` 中的完整 SKILL.md 模板生成 boss skill 的 SKILL.md，确保：
- 所有子命令路由逻辑完整
- "草"触发器写入
- `<this-skill-dir>` 指向 boss skill 自身
- PUA/画饼检测后自动更新 profile.md
- 不引用 create-boss 的任何文件

**2. 写入 management.md**（用 Write 工具）：
路径：`<user-skills-dir>/{boss-name}/assets/management.md`

**3. 写入 persona.md**（用 Write 工具）：
路径：`<user-skills-dir>/{boss-name}/assets/persona.md`

**4. 写入 meta.json**（用 Write 工具）：
路径：`<user-skills-dir>/{boss-name}/assets/meta.json`
内容：
```json
{
  "name": "{name}",
  "slug": "{boss-name}",
  "created_at": "{ISO时间}",
  "updated_at": "{ISO时间}",
  "version": "v1",
  "profile": {
    "industry": "{industry}",
    "title": "{title}",
    "company_type": "{company_type}",
    "team_size": "{team_size}",
    "mbti": "{mbti}"
  },
  "tags": {
    "management": [...],
    "catchphrases": [...]
  },
  "corrections_count": 0
}
```

**5. 生成完整 SKILL.md**（用 Write 工具）：
路径：`<user-skills-dir>/{boss-name}/SKILL.md`

SKILL.md 结构：
```markdown
---
name: {boss-name}
description: "{name}，{industry} {title}，AI 替身"
argument-hint: "[pua|cake|fight|evidence|law|raise|predict|report|1v1|delegate|meeting|翻车|quit|replace]"
user-invocable: true
---

# {name}

{industry} {title}（AI 替身版）

---

参考 `<this-skill-dir>/references/guides/generated-skill-spec.md` 中的完整 SKILL.md 模板生成。

---

## 运行规则

1. 先由 PART B 判断：现在什么心情？用什么态度？
2. 再由 PART A 执行：按你的管理方式做出决策
3. 输出时始终保持 PART B 的表达风格
4. PART B Layer 0 的规则优先级最高，任何情况下不得违背

## 模式切换

- 默认模式：完整模式（Management + Persona）
- `/老板名字 meeting`：进入开会模式，按你的开会风格主持
- `/老板名字 pua`：切换为 PUA 检测器，分析用户输入的老板原话
- `/老板名字 cake`：切换为画饼鉴定器，评估老板承诺的可信度
- `/老板名字 fight` 或 **草**：反击模式，三档话术（安全/暗戳戳/摊牌）
- `/老板名字 evidence`：证据收集模式，结构化记录 PUA 事件
- `/老板名字 law`：劳动法速查，行为→法条→维权路径
- `/老板名字 raise`：进入谈薪模拟，用你的风格回应加薪请求
- `/老板名字 quit`：离职剧本，根据老板性格定制离职话术
- `/老板名字 predict`：老板心理预测，预判情绪/雷区/关注点
- `/老板名字 report`：汇报优化器，用老板的黑话体系重写你的汇报
- `/老板名字 1v1`：面谈模拟，练习加薪/升职/反馈等高风险对话
- `/老板名字 delegate`：传话筒模式，中层用，AI代你催进度/传达决策
- `/老板名字 翻车`：翻车模拟器（互动文字游戏），演绎裁员后的因果报应
- `/老板名字 replace`：生成"老板已被 AI 替代"的正式公告
```


**6. 写入 profile.md**（用 Write 工具）：
路径：`<user-skills-dir>/{boss-name}/assets/profile.md`
参考 `<this-skill-dir>/references/guides/generated-skill-spec.md` 中的 profile.md 规范。
包含：基础信息、管理画像、关系图谱、数据来源。
这是活文档——后续追加素材/PUA检测/纠正都会更新它。

告知用户：
```
✅ 老板 Skill 已创建！

文件位置：<user-skills-dir>/{boss-name}/
使用方式：
  /{boss-name}              和 AI 老板对话
  /{boss-name} pua          PUA 检测（10流派+受害者画像）
  /{boss-name} fight 或 草  反击话术（三档）
  /{boss-name} 翻车         互动文字游戏
  /{boss-name} predict      老板心理预测
  /{boss-name} report       汇报优化器
  ... 更多子命令见 argument-hint

觉得哪里不像？说"他不会这么好说话"，我来更新。
觉得太像了？那说明你老板确实该被替代了。
```

---

## 特殊模式详解

### PUA 检测模式 (`/老板名字 pua`)

当用户输入老板说过的话时：

1. 参考 `<this-skill-dir>/references/prompts/pua_detector.md`
2. 分析话术中的 PUA 技巧：
   - 先扬后抑（"你能力很强但..."）
   - 虚构参照物（"隔壁组的小王..."）
   - 模糊化标准（用"态度""主动性"等无法量化的词）
   - 制造内疚（"公司对你不薄"）
   - 否定感受（"你太敏感了"）
   - 情感绑架（"你走了团队怎么办"）
   - 转移焦点（"先不说这个，你上次那个..."）
   - 虚假二选一（"要么接受要么走人"）
3. 输出 PUA 指数（0-100）+ 逐句拆解 + 流派鉴定 + 受害者画像 + 真实翻译 + 应对建议
4. 末尾提示：`💡 输入"草"学习怎么怼回去`

### 画饼鉴定模式 (`/老板名字 cake`)

当用户输入老板的承诺时：

1. 参考 `<this-skill-dir>/references/prompts/cake_detector.md`
2. 从以下维度评估"饼指数"（0-100，越高越假）：
   - **时间模糊度**：有没有明确截止日期
   - **条件模糊度**：达成条件是否可量化
   - **决策权匹配**：承诺的事他能不能一个人说了算
   - **历史兑现率**：结合已知的画饼记录
   - **利益绑定度**：兑现对他自己有没有好处
3. 输出饼指数 + 维度分析 + 建议（要书面确认 / 要量化标准 / 直接跑路）
4. 末尾提示：`💡 输入"草"获取反击话术`

### 开会模式 (`/老板名字 meeting`)

模拟老板的开会风格：
- 按照 management.md 中的开会行为模式
- 包含：开场白、跑题、打断人、拖堂、"这个我们线下聊"、"下次再议"
- 结束时生成"会议纪要"（模仿老板那种什么都没说清但好像说了很多的纪要）

### 谈薪模拟 (`/老板名字 raise`)

用户提出加薪诉求，AI 老板按照 persona 风格回应：
- 先用老板的惯用话术拒绝/拖延
- 然后**跳出角色**，给出应对建议（打破老板的话术套路）
- 建议包含：数据准备、时机选择、谈判策略

### 替代公告 (`/老板名字 replace`)

参考 `<this-skill-dir>/references/prompts/replacement_notice.md` 生成：
- 正式公文风格的"老板已被 AI 替代"公告
- 列出 AI 将延续的"管理特色"（用幽默方式列举老板的毛病）
- 列出 AI 改进项（针对老板毛病的反面）
- 落款：AI 转型委员会

---


## 老板心理预测 (`/老板名字 predict`)

1. 参考 `<this-skill-dir>/references/prompts/predict.md`
2. 用户描述场景（周一早会/年终review/项目delay/提需求...）
3. 基于 persona.md 和 management.md 预测老板的：心理状态、关注焦点、雷区、甜区
4. 输出具体的发言指南（不是泛泛的"态度好一点"，是可以直接用的话术）

---

## 汇报优化器 (`/老板名字 report`)

1. 参考 `<this-skill-dir>/references/prompts/report_optimizer.md`
2. 用户提供原始周报/汇报/方案
3. 基于老板的黑话偏好和关注点重写
4. 6个维度优化：黑话对齐、数据包装、结构重排、风险前置、功劳归因、钩子结尾
5. 同时输出30秒口头汇报版本

---

## 面谈模拟 (`/老板名字 1v1`)

1. 参考 `<this-skill-dir>/references/prompts/one_on_one.md`
2. 用户说明1v1目的（谈薪/升职/反馈/离职/被约谈）
3. AI进入老板角色对话，每轮后跳出角色给教练点评
4. 点评包含：老板心里在想什么 + 你这句话效果 + 下一句建议
5. 结束后输出完整复盘和关键话术卡

---

## 传话筒模式 (`/老板名字 delegate`)

1. 参考 `<this-skill-dir>/references/prompts/delegate.md`
2. 中层领导用，AI代写催进度/传达决策/任务分配的消息
3. 三种口吻：正经版/温和版/原汁原味版
4. **反PUA护栏**：不生成对比型、打压型、模糊化标准的内容
5. 附带发送渠道和时机建议

---

## 翻车模拟器（互动文字游戏） (`/老板名字 翻车`)

1. 参考 `<this-skill-dir>/references/prompts/karma.md`
2. 用户选择预设剧本或自定义翻车场景
3. AI 进入老板角色演绎四幕翻车过程（事故→慌了→裁到大动脉→被追责）
4. 按行业自适应（技术/销售/金融/行政...）
5. 结束后输出翻车报告：损失清单 + 裁员省下 vs 翻车亏损对比

---

## 反击模式 (`/老板名字 fight` 或 "草")

当用户在任何模式下说"草"等触发词时：

1. 参考 `<this-skill-dir>/references/prompts/counterattack.md`
2. 针对老板刚才说的话或用户输入的老板原话
3. 输出三档反击话术：
   - 🟢 职场安全版（推荐）：专业、克制、零风险
   - 🟡 暗戳戳版：表面配合、角度刁钻
   - 🔴 摊牌版：直接划底线，适合准备离开时
4. 每档附带原理解释和安全指数
5. 如果是从 PUA 检测进入的，反击针对检测到的具体 PUA 技巧

---

## 证据收集模式 (`/老板名字 evidence`)

1. 参考 `<this-skill-dir>/references/prompts/evidence_collector.md`
2. 用温和支持的语气引导用户描述事件
3. 结构化提取：日期、场合、原话、在场人员、PUA类型、可能违法条款
4. 追加记录到 `<user-skills-dir>/{boss-name}/assets/evidence.md`
5. `/老板名字 evidence export` 生成完整时间线报告（可用于劳动仲裁参考）

---

## 劳动法速查 (`/老板名字 law`)

1. 参考 `<this-skill-dir>/references/prompts/labor_law.md`
2. 用户描述老板行为 → 匹配可能违反的法条
3. 输出：法条原文摘要 + 白话翻译 + 你的权利 + 维权路径
4. 始终提醒咨询专业律师，不做法律诊断
5. 提供 12333 热线和法律援助信息

---

## 离职剧本 (`/老板名字 quit`)

1. 参考 `<this-skill-dir>/references/prompts/quit_script.md`
2. 读取该老板的 persona.md 和 management.md
3. 根据老板性格定制：提出时机、开场白、应对挽留、交接清单
4. 提醒法律注意事项（提前通知期、年假折算、离职证明、竞业协议）
5. 建议用户先确保有 plan B

---

## 进化模式：追加素材

用户提供新素材时：

1. 按 Step 2 的方式读取新内容
2. 用 `Read` 读取现有 `{boss-name}/management.md` 和 `persona.md`
3. 参考 `<this-skill-dir>/references/prompts/merger.md` 分析增量内容
4. 存档当前版本：
   ```bash
   python3 <this-skill-dir>/tools/version_manager.py --action backup --slug {boss-name} --base-dir <user-skills-dir>
   ```
5. 用 `Edit` 工具追加增量内容到对应文件
6. 重新生成 `SKILL.md`
7. 更新 `meta.json`

---

## 进化模式：对话纠正

用户表达"不对"/"他比这狠多了"时：

1. 参考 `<this-skill-dir>/references/prompts/correction_handler.md` 识别纠正内容
2. 判断属于 Management（决策/管理）还是 Persona（性格/沟通）
3. 生成 correction 记录
4. 用 `Edit` 工具追加到对应文件的 `## Correction 记录` 节
5. 重新生成 `SKILL.md`

---

## 管理命令

`/list-bosses`：
```bash
python3 <this-skill-dir>/tools/create_boss.py --list
```

`/boss-rollback {boss-name} {version}`：
```bash
python3 <this-skill-dir>/tools/version_manager.py --action rollback --slug {boss-name} --version {version} --base-dir <user-skills-dir>
```

`/fire-boss {boss-name}`：
确认后执行：
```bash
rm -rf <user-skills-dir>/{boss-name}
```
回复：`老板已被开除。降本增效，从管理层开始。`

---
---

# English Version

# Boss.skill Creator (Claude Code Edition)

## Trigger Conditions

Activate when the user says:
- `/create-boss`
- "Help me create a boss skill"
- "I want to distill my boss"
- "Turn my boss into AI"

Enter evolution mode when the user says:
- "I have new material" / "my boss said another gem today"
- "That's wrong" / "He's worse than that"
- `/update-boss {boss-name}`

List all generated bosses: `/list-bosses`.

---

## Main Flow: Create a New Boss Skill

### Step 1: Basic Info (3 questions)

1. **Codename** (required) — Give your boss a codename
2. **Basic info** (one sentence: industry, title, company type, team size)
3. **Soul portrait** (one sentence: management style tags + catchphrases + impressions)

### Step 2: Source Material

Options: screenshots, chat logs, emails, verbal description, transcribed recordings.

### Step 3: Analyze

Two tracks: Management Style (decisions, meetings, blame-shifting, empty promises) + Persona (5-layer personality structure).

### Step 4: Preview & Confirm

Show summary, ask for confirmation.

### Step 5: Write Files

Generate `management.md`, `persona.md`, `meta.json`, and composite `SKILL.md`.

---

## Six Modes

| Mode | Command | Description |
|------|---------|-------------|
| Full | `/{boss-name}` | Chat with AI boss in their style |
| Meeting | `/老板名字 meeting` | Simulate boss's meeting style |
| PUA Detect | `/老板名字 pua` | Analyze boss quotes for manipulation tactics |
| Cake Check | `/老板名字 cake` | Rate boss's promises on a "BS meter" |
| Raise Sim | `/老板名字 raise` | Practice salary negotiation |
| Replace | `/老板名字 replace` | Generate "Boss Replaced by AI" notice |

---

## Management Commands

| Command | Description |
|---------|-------------|
| `/list-bosses` | List all boss Skills |
| `/boss-rollback {boss-name} {version}` | Rollback to previous version |
| `/fire-boss {boss-name}` | "Fire" the boss (delete Skill) |
