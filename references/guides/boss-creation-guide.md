# Boss Skill 创建指南

## 工作流程

```
用户: /create-boss
  ↓
Step 1: 输入老板代号 + 基本信息 + 灵魂画像
  ↓
Step 2: 提供素材（截图/聊天记录/手动描述）
  ↓
Step 3: AI 分析，提取 Management Style + Persona
  ↓
Step 4: 预览确认
  ↓
Step 5: 生成独立 Skill（复制 prompts + 生成数据 + 写 SKILL.md）
  ↓
用户: /王总           和 AI 老板对话
用户: /王总 pua       PUA 检测
用户: /王总 翻车      互动文字游戏
```

## 关键原则

**生成的 boss skill 必须完全自包含。**

- 用户把王总文件夹复制给同事 → 同事不需要装 create-boss 就能用
- 所有 prompt 模板在创建时复制到 boss skill 的 assets/prompts/
- SKILL.md 中的 `<this-skill-dir>` 指向 boss skill 自身，不是 create-boss
- 不依赖 create-boss 的 tools/ 脚本

## 多老板支持

可以为不同老板创建多个 skill：
- `/create-boss` → 创建"王总"
- `/create-boss` → 创建"李总"
- `/list-bosses` → 查看所有老板

## 进化机制

创建后可持续补充数据：
- 追加素材 → 重新分析，更新 management.md / persona.md / profile.md
- 对话纠正 → 用户说"他不会这样" → 追加到 profile.md Correction 记录
- PUA 检测 → 自动记录到 profile.md 的 PUA 历史
- 画饼鉴定 → 自动记录到 profile.md 的画饼历史

## 创建完成 Checklist

| # | 检查项 | 说明 |
|---|--------|------|
| 1 | SKILL.md 存在 | frontmatter 完整（name, description, argument-hint, user-invocable） |
| 2 | assets/management.md | 管理风格分析结果 |
| 3 | assets/persona.md | 5层人格结构 |
| 4 | assets/profile.md | 多维档案（基础信息+画像+图谱） |
| 5 | assets/evidence.md | 空模板 |
| 6 | assets/prompts/ 有 12 个文件 | 从 create-boss 复制的运行时 prompt |
| 7 | 子命令路由完整 | SKILL.md 中 16 个子命令都有明确指令 |
| 8 | "草"触发器 | 写在 SKILL.md 中 |
| 9 | 自动更新 profile | PUA/画饼检测后自动追加记录 |
| 10 | 零外部依赖 | 不引用 create-boss 的任何文件 |

详细的文件结构和 SKILL.md 模板见 `generated-skill-spec.md`。
