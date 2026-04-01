# 安装指南

## Claude Code

```bash
# 方式一：安装到当前项目（在 git 仓库根目录执行）
git clone https://github.com/nicepkg/boss-skill <your-skills-dir>/create-boss

# 方式二：安装到全局（所有项目都能用）
git clone https://github.com/nicepkg/boss-skill <your-global-skills-dir>/create-boss
```

## OpenClaw

```bash
git clone https://github.com/nicepkg/boss-skill ~/.openclaw/workspace/skills/create-boss
```

## 依赖

核心功能零依赖，只需 Python 3.9+。

## 使用

安装完成后，在 Claude Code 中输入：

```
/create-boss
```

按提示操作即可。

## 卸载

```bash
# Claude Code（当前项目）
rm -rf <your-skills-dir>/create-boss

# Claude Code（全局）
rm -rf <your-global-skills-dir>/create-boss

# OpenClaw
rm -rf ~/.openclaw/workspace/skills/create-boss
```

## 常见问题

**Q: Skill 没有出现在命令列表中？**
A: 确保 clone 到了 AI CLI 工具的 skills 目录下，且 `SKILL.md` 在目录根下。

**Q: 生成的老板 Skill 在哪？**
A: 在 `<user-skills-dir>/{boss-name}/` 目录下。

**Q: 数据安全吗？**
A: 所有处理都在本地完成，不会上传到任何服务器。生成的 `<user-skills-dir>/` 目录已在 `.gitignore` 中。
