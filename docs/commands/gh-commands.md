---
title: GitHub (gh) Commands 使用指南
description: GitHub CLI 集成命令的完整使用文档
tags: [commands, gh, github, git, workflow]
created: 2025-11-04
---

# GitHub (gh) Commands 使用指南

GitHub Commands 是一组集成 GitHub CLI 的专业命令,用于简化 GitHub 工作流,包括 PR 审查、Issue 修复和智能 commit。所有命令都采用 `/gh:` 前缀。

## 📋 目录

- [命令概览](#命令概览)
- [详细命令说明](#详细命令说明)
- [最佳实践](#最佳实践)

## 命令概览

| 命令 | 描述 | 允许工具 |
|------|------|----------|
| `/gh:review-pr` | 审查 GitHub Pull Request,提供详细代码分析 | Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*) |
| `/gh:fix-issue` | 分析并修复 GitHub Issue | Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*) |
| `/gh:gh-commit` | 智能 Commit,遵循 Conventional Commits 标准 | Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*) |

---

## 详细命令说明

### /gh:review-pr

**描述**: 审查 GitHub Pull Request,提供详细的代码分析
**参数提示**: `[pr-number]`
**允许工具**: Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*)

**使用方法**:
```bash
/gh:review-pr [pr-number]
```

**工作流程**:

1. **获取 PR 信息**
   - 如未提供 PR 编号,使用 `gh pr list` 显示所有开放的 PR
   - 如提供 PR 编号,使用 `gh pr view <pr-number>` 获取 PR 详情

2. **分析变更**
   - 使用 `gh pr diff <pr-number>` 获取代码差异
   - 全面分析代码变更

3. **提供审查报告**
   包括以下内容:
   - PR 功能概述
   - 代码质量和风格分析
   - 具体改进建议
   - 潜在问题和风险

4. **发布审查评论** (可选)
   - 仅关注建议、代码变更和潜在问题
   - 不重复 PR 描述内容
   - 使用 `gh api` 发布行内评论

**审查重点**:
- ✅ **代码正确性**: 逻辑是否正确,是否有潜在 bug
- ✅ **项目约定**: 是否遵循项目编码规范和风格
- ✅ **性能影响**: 变更对性能的影响
- ✅ **测试覆盖**: 是否有足够的测试覆盖
- ✅ **安全考虑**: 是否存在安全隐患

**使用示例**:

**1. 审查特定 PR**
```bash
/gh:review-pr 123
```
审查编号为 123 的 Pull Request,提供详细分析报告。

**2. 查看所有待审查 PR**
```bash
/gh:review-pr
```
列出所有开放的 Pull Request,方便选择审查对象。

**gh 命令参考**:
```bash
# 列出所有 PR
gh pr list

# 查看 PR 详情
gh pr view 78

# 查看 PR 代码变更
gh pr diff 78

# 发布审查评论到特定文件行
gh api repos/OWNER/REPO/pulls/PR_NUMBER/comments \
    --method POST \
    --field body="[your-comment]" \
    --field commit_id="[commitID]" \
    --field path="path/to/file" \
    --field line=lineNumber \
    --field side="RIGHT"

# 获取 commit ID
gh api repos/OWNER/REPO/pulls/PR_NUMBER --jq '.head.sha'
```

---

### /gh:fix-issue

**描述**: 分析并修复 GitHub Issue
**参数提示**: `[issue-number]`
**允许工具**: Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*)

**使用方法**:
```bash
/gh:fix-issue [issue-number]
```

**完整工作流**:

#### 1. PLAN (规划阶段)

**a. 获取 Issue 详情**
```bash
gh issue view <issue-number>
```

**b. 理解问题**
- 分析 Issue 描述
- 必要时提出澄清问题

**c. 了解历史背景**
- 搜索 scratchpads 中与 Issue 相关的先前思考
- 搜索相关 PR,查看是否有历史记录
- 在代码库中搜索相关文件

**d. 任务分解**
- 深入思考如何将 Issue 分解为一系列小而可管理的任务

**e. 文档化计划**
- 在新的 scratchpad 中记录计划
- 在文件名中包含 Issue 名称
- 在 scratchpad 中包含 Issue 链接

#### 2. CREATE (创建阶段)

**a. 创建新分支**
```bash
git checkout -b fix/issue-<issue-number>-<description>
```

**b. 实现解决方案**
- 按照计划,以小而可管理的步骤解决 Issue
- 每完成一个步骤后提交变更

**c. 提交变更**
```bash
git commit -m "fix(scope): description

Fixes #<issue-number>"
```

#### 3. TEST (测试阶段)

**a. UI 测试** (如果修改了 UI)
- 如果 Puppeteer 在工具列表中,使用 Puppeteer MCP 测试 UI 变更

**b. 单元测试**
- 编写单元测试描述代码的预期行为

**c. 完整测试套件**
- 运行完整测试套件,确保没有破坏任何功能

**d. 修复失败测试**
- 如果测试失败,进行修复
- 确保所有测试通过后再进行下一步

#### 4. OPEN PULL REQUEST (开启 PR)

**a. 创建 PR**
```bash
gh pr create --title "Fix: <issue-title>" \
             --body "Fixes #<issue-number>

## Summary
<1-3 bullet points>

## Changes
- <change 1>
- <change 2>

## Testing
- <test approach>
"
```

**b. 请求审查**
- 请求团队成员审查 PR

**使用示例**:

**1. 修复特定 Issue**
```bash
/gh:fix-issue 456
```
分析并修复编号为 456 的 Issue,按照完整工作流执行。

**2. 修复带描述的 Issue**
```bash
/gh:fix-issue 789
```
获取 Issue 789 的详情,理解问题,制定计划并实施修复。

**最佳实践**:
- 📝 始终记录计划和思考过程
- 🔍 在开始编码前理解问题的完整上下文
- 🧪 确保测试覆盖新代码
- 💬 提出澄清问题,不要假设
- 🔄 小步提交,频繁提交

---

### /gh:gh-commit

**描述**: 智能 Commit 专家,创建遵循 Conventional Commits 标准的良好组织的逻辑提交
**允许工具**: Write, Read, LS, Glob, Grep, Bash(gh:\*), Bash(git:\*)

**使用方法**:
```bash
/gh:gh-commit                    # 分析并提交
/gh:gh-commit "description"      # 使用描述信息指导消息
```

**完整工作流**:

#### 1. Safety & Branch Check (安全和分支检查)

**a. 检查当前分支**
```bash
git branch --show-current
```

**b. 分支安全检查**

**如果在 main/master 分支:**
- ⚠️ **停止**: 永远不要在 main 分支上提交
- 询问: "你正在处理什么功能/修复?"
- 创建分支: `git checkout -b {type}/{description}`
  - 例如: `feat/add-yaml-support`

**如果在功能分支:**
- ✅ 继续分析

**c. 检查变更**
```bash
git status --porcelain
git diff --stat
```

#### 2. Analyze & Batch Changes (分析和批处理变更)

**a. 读取用户请求**
理解目的 (feature, fix, refactor, docs 等)

**b. 按类型和范围分类变更**:

- **feat/fix**: 核心实现,主要逻辑
- **test**: 测试文件,测试更新
- **docs**: README, docstrings, 文档
- **refactor**: 不改变行为的代码清理
- **chore**: 依赖, 构建配置, 工具

**c. 批处理规则**:
- 保持相关变更在一起
- 分离关注点 (不混合不相关代码)
- 每次提交应该是原子性的
- 如果测试依赖实现,一起提交

#### 3. Create Commits (创建提交)

**a. 按组添加文件**:
```bash
git add file1.py file2.py file3.py
```
- ✅ 仅添加当前批次的文件
- ❌ 永不使用 `git add .`

**b. 使用 Conventional 格式提交**:
```bash
git commit -m "$(cat <<'EOF'
type(scope): description

Optional body explaining why this change was made.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Commit 类型**:
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档变更
- `test`: 测试相关
- `refactor`: 重构代码
- `style`: 代码风格 (不影响代码运行的变动)
- `perf`: 性能优化
- `chore`: 构建过程或辅助工具的变动
- `ci`: CI 配置文件和脚本的变动

**Scope 示例**:
- `anthropic`, `openai`, `validation`, `streaming`, `cli`, `docs`

**Description 规则**:
- 祈使语气: "add feature" 而非 "added feature"
- 简洁但描述性强
- 不加结尾句号
- 简单、清晰的语言

#### 4. Summary & Next Steps (总结和后续步骤)

**a. 显示创建的提交**
```bash
git log main..HEAD --oneline
git diff main...HEAD --stat
```

**b. 报告内容**:
- 列出创建的提交
- 解释批处理理由
- 建议: push, 创建 PR, 或继续工作

**使用示例**:

**Example 1: 功能提交**
```bash
/gh:gh-commit

# 输出:
# 🔍 Analyzing changes...
#
# Branch: feat/add-yaml-support
# Changed: 8 files
#
# 📦 Batches:
#   1. Core (3 files) - feat(yaml)
#   2. Tests (3 files) - test(yaml)
#   3. Docs (2 files) - docs(yaml)
#
# ✅ Creating commits...
#
# 📝 feat(yaml): add MD_YAML mode for YAML extraction
#    Files: instructor/mode.py, instructor/client_openai.py, instructor/yaml_handler.py
#    ✓ abc123f
#
# 📝 test(yaml): add tests for MD_YAML mode
#    Files: tests/test_yaml.py, tests/fixtures/yaml_samples.py
#    ✓ def456a
#
# 📝 docs(yaml): document MD_YAML usage
#    Files: README.md, docs/concepts/yaml-mode.md
#    ✓ ghi789b
#
# ✨ Summary: 3 commits, 8 files changed
#
# Next: git push -u origin feat/add-yaml-support
```

**Example 2: Bug 修复**
```bash
feat(anthropic): add support for Claude 3.5 Sonnet

Implements client wrapper with streaming and function calling.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

**Example 3: 修复验证问题**
```bash
fix(validation): handle empty response arrays

Previously crashed on empty arrays. Now returns empty list.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

**Example 4: 测试提交**
```bash
test(gemini): add validation tests for JSON mode

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

**Example 5: 文档更新**
```bash
docs(README): update installation instructions

Add UV installation method and Python 3.9+ requirement.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

**特殊情况处理**:

**多个功能**: 询问是分开提交还是一起提交

**Breaking Changes**: 在 body 中添加 `BREAKING CHANGE:` 或使用 `feat!:`

**大型重构**: 询问用户批处理偏好

**Pre-commit hooks 失败**: 显示输出,询问修复应该在同一个还是单独的提交中

**项目感知**:
```bash
# 在提交前检查
git log --oneline -10  # 遵循现有模式
```

如果存在,读取: `CLAUDE.md`, `CONTRIBUTING.md`, `.gitmessage`

---

## 最佳实践

### PR 审查最佳实践

1. **系统化审查**
   - 先理解 PR 的整体目的
   - 然后深入到具体代码细节
   - 关注关键路径和边界情况

2. **建设性反馈**
   - 提供具体的改进建议,而非泛泛而谈
   - 解释"为什么"而不只是"什么"
   - 认可好的代码实践

3. **安全和性能**
   - 特别关注认证和授权逻辑
   - 识别潜在的性能瓶颈
   - 检查资源泄漏风险

### Issue 修复最佳实践

1. **理解优先**
   - 在编码前充分理解问题
   - 查看相关历史记录和上下文
   - 必要时提出澄清问题

2. **小步前进**
   - 将大问题分解为小任务
   - 每个小任务独立提交
   - 保持提交历史清晰

3. **测试驱动**
   - 先写测试描述预期行为
   - 实现代码使测试通过
   - 确保不破坏现有功能

### Commit 最佳实践

1. **遵循约定**
   - 使用 Conventional Commits 格式
   - 保持 commit message 简洁明了
   - 在 body 中解释"为什么"

2. **原子性提交**
   - 每次提交只做一件事
   - 相关变更放在一起
   - 避免混合不相关的变更

3. **分支策略**
   - 永远不要直接在 main/master 提交
   - 使用描述性的分支名
   - 遵循 `type/description` 格式

### GitHub CLI 使用技巧

**常用命令**:
```bash
# 查看所有 PR
gh pr list --state all

# 查看自己的 PR
gh pr list --author "@me"

# 查看特定 PR 的检查状态
gh pr checks <pr-number>

# 批准 PR
gh pr review <pr-number> --approve

# 请求变更
gh pr review <pr-number> --request-changes

# 合并 PR
gh pr merge <pr-number> --squash

# 查看 Issue 列表
gh issue list

# 创建 Issue
gh issue create --title "Bug: ..." --body "..."

# 关闭 Issue
gh issue close <issue-number>
```

---

## 相关资源

- [GitHub CLI 官方文档](https://cli.github.com/manual/)
- [Conventional Commits 规范](https://www.conventionalcommits.org/)
- [[Level-3-Extension-Systems/Slash-Commands-Guide|Slash Commands 完整指南]]

---

## 总结

GitHub Commands 提供了从 PR 审查、Issue 修复到智能 Commit 的完整 GitHub 工作流支持。通过合理使用这些命令,可以:

- ✅ 提高代码审查质量和效率
- ✅ 系统化地修复 Issue
- ✅ 创建清晰、规范的 Git 历史
- ✅ 遵循团队和社区最佳实践

建议学习顺序:
1. **入门**: gh-commit (智能提交)
2. **进阶**: review-pr (PR 审查)
3. **高级**: fix-issue (完整 Issue 修复流程)
