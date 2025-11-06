---
title: Claude Code 自定义命令总览
description: 项目中所有自定义命令的完整索引
tags: [commands, overview, index]
created: 2025-11-04
---

# Claude Code 自定义命令总览

本文档提供了项目中所有自定义 Slash Commands 的完整索引和快速参考。

## 📋 目录

- [命令组织结构](#命令组织结构)
- [主要命令组](#主要命令组)
- [独立命令](#独立命令)
- [快速查找](#快速查找)

## 命令组织结构

项目中的自定义命令按照功能组织为以下结构:

```
.claude/commands/
├── sc/          # SuperClaude - 综合开发工作流 (24 个命令)
├── gh/          # GitHub 集成 (3 个命令)
├── kiro/        # Kiro 开发助手 (5 个命令)
├── cc/          # Claude Code 工具
├── cook/        # 开发 Cookbook
├── BMad/        # Business Madness 框架
├── eureka.md    # 技术突破文档化
├── think-harder.md      # 增强分析思考
├── think-ultra.md       # 超级分析思考
├── reflection.md        # 任务反思
├── reflection-harder.md # 深度反思
├── de-slop.md          # 代码清理
└── rule2hook.md        # 规则转 Hook
```

**统计信息**:
- 总命令文件数: 112+
- 主要命令组: 6 个
- 独立命令: 7 个

## 主要命令组

### 🚀 SuperClaude (sc) - 24 个命令

**完整文档**: [[sc-commands|SuperClaude Commands 完整指南]]

SuperClaude 是最强大的命令组,提供全面的开发工作流支持。

**命令分类**:

**Utility (工具类) - 8 个**
- `/sc:help` - 命令帮助
- `/sc:analyze` - 代码分析
- `/sc:build` - 项目构建
- `/sc:design` - 架构设计
- `/sc:document` - 文档生成
- `/sc:git` - Git 操作
- `/sc:test` - 测试执行
- `/sc:troubleshoot` - 问题诊断

**Workflow (工作流) - 4 个**
- `/sc:cleanup` - 代码清理
- `/sc:explain` - 代码解释
- `/sc:implement` - 功能实现
- `/sc:improve` - 代码改进

**Orchestration (编排) - 2 个**
- `/sc:brainstorm` - 需求探索
- `/sc:workflow` - 工作流生成

**Special (特殊) - 5 个**
- `/sc:estimate` - 开发估算
- `/sc:index` - 知识库索引
- `/sc:select-tool` - 工具选择
- `/sc:spawn` - 任务分解
- `/sc:task` - 任务管理

**Session (会话) - 3 个**
- `/sc:load` - 加载上下文
- `/sc:reflect` - 任务反思
- `/sc:save` - 保存会话

**Analysis (分析) - 2 个**
- `/sc:spec-panel` - 规范审查
- `/sc:business-panel` - 业务分析

**特色功能**:
- 多 MCP Server 集成 (Sequential, Context7, Magic, Playwright, Morphllm, Serena)
- 智能 Persona 激活
- 跨会话持久化
- 系统化任务编排

---

### 🐙 GitHub (gh) - 3 个命令

**完整文档**: [[gh-commands|GitHub Commands 使用指南]]

专业的 GitHub 工作流集成命令。

**命令列表**:
- `/gh:review-pr` - PR 审查,提供详细代码分析
- `/gh:fix-issue` - Issue 修复,完整工作流
- `/gh:gh-commit` - 智能 Commit,遵循 Conventional Commits

**主要功能**:
- GitHub CLI 深度集成
- Conventional Commits 标准
- 自动化 PR 审查
- 系统化 Issue 修复流程

---

### 🎯 Kiro - 5 个命令

Kiro 是一个轻松、开发者友好的助手系统。

**命令列表**:
- `/kiro:vibe` - 快速开发协助
- `/kiro:design` - 功能设计文档
- `/kiro:spec` - 完整功能规范
- `/kiro:task` - 任务列表生成
- `/kiro:execute` - 执行特定任务

**特点**:
- 轻松的开发者风格
- 从设计到实现的完整流程
- 结构化任务管理

---

### 🎨 Claude Code (cc)

Claude Code 工具命令集。

**功能领域**:
- 命令创建和管理
- 配置辅助
- 工具集成

---

### 📚 Cook

开发 Cookbook 和实践指南。

**功能领域**:
- 最佳实践
- 代码模式
- 实现指南

---

### 💼 BMad (Business Madness)

业务敏捷开发框架,包含多个 Agents 和 Tasks。

**Agents** (10+):
- bmad-master - 主控制器
- bmad-orchestrator - 编排器
- architect - 架构师
- analyst - 分析师
- pm - 项目经理
- po - 产品负责人
- dev - 开发人员
- qa - 质量保证
- sm - Scrum Master
- ux-expert - UX 专家

**Tasks** (30+):
包括需求收集、Epic 创建、Story 创建、文档生成等完整的敏捷开发任务。

---

## 独立命令

### /eureka
**描述**: 捕获技术突破并转化为可操作、可重用的文档
**参数**: `[breakthrough description]`

**使用场景**:
- 实现重大技术突破时
- 发现重要性能优化时
- 找到创新解决方案时

**示例**:
```bash
/eureka "Reduced API response time from 2s to 100ms by implementing request batching"
```

---

### /think-harder
**描述**: 增强分析思考,用于复杂问题
**参数**: `[problem or question]`

**使用场景**:
- 需要深度分析复杂问题时
- 多维度评估方案时
- 系统化思考时

**方法论**:
- 问题澄清
- 多维度分析
- 批判性评估
- 综合整合

---

### /think-ultra
**描述**: 超级综合分析思考,用于最复杂的问题
**参数**: `[complex problem or question]`

**使用场景**:
- 极其复杂的架构决策
- 多系统交互分析
- 战略级别的技术决策

**特点**:
- 更深层次的分析
- 更多的视角
- 更全面的评估

---

### /reflection
**描述**: 分析和改进 Claude Code 指令
**参数**: `none`

**使用场景**:
- 审查项目配置
- 优化 CLAUDE.md
- 改进工作流

---

### /reflection-harder
**描述**: 综合会话分析和学习捕获
**参数**: `none`

**使用场景**:
- 会话结束时的深度回顾
- 捕获重要学习和洞察
- 文档化最佳实践

---

### /de-slop
**描述**: 清理和优化代码质量

**使用场景**:
- 移除冗余代码
- 优化代码风格
- 提高代码质量

---

### /rule2hook
**描述**: 将规则转换为 Hook

**使用场景**:
- 自动化规则执行
- 创建自定义 Hooks
- 工作流优化

---

## 快速查找

### 按使用频率

**高频使用**:
- `/sc:implement` - 功能实现
- `/sc:test` - 测试执行
- `/gh:gh-commit` - 智能提交
- `/sc:analyze` - 代码分析
- `/sc:troubleshoot` - 问题诊断

**中频使用**:
- `/sc:document` - 文档生成
- `/sc:improve` - 代码改进
- `/gh:review-pr` - PR 审查
- `/sc:explain` - 代码解释
- `/kiro:spec` - 功能规范

**专业使用**:
- `/sc:brainstorm` - 需求探索
- `/sc:business-panel` - 业务分析
- `/sc:spec-panel` - 规范审查
- `/sc:spawn` - 任务编排
- `/think-ultra` - 超级思考

### 按应用场景

**代码开发**:
- `/sc:implement`, `/sc:improve`, `/kiro:execute`

**代码审查**:
- `/gh:review-pr`, `/sc:analyze`

**问题解决**:
- `/sc:troubleshoot`, `/gh:fix-issue`, `/think-harder`

**文档编写**:
- `/sc:document`, `/sc:index`, `/eureka`

**架构设计**:
- `/sc:design`, `/sc:brainstorm`, `/kiro:design`

**测试质量**:
- `/sc:test`, `/sc:cleanup`, `/de-slop`

**项目管理**:
- `/sc:task`, `/sc:estimate`, `/sc:workflow`

**学习反思**:
- `/reflection`, `/reflection-harder`, `/sc:reflect`

### 按复杂度

**Low**: help, git
**Basic**: analyze, design, document, troubleshoot
**Standard**: cleanup, estimate, explain, implement, improve, index, load, reflect, save
**Enhanced**: build, test, spec-panel
**Advanced**: brainstorm, task, workflow
**High**: select-tool, spawn
**Complex**: business-panel

---

## MCP Server 支持

不同命令对 MCP Server 的使用情况:

### Sequential MCP
analyze, brainstorm, cleanup, estimate, explain, implement, improve, index, spec-panel, task, workflow

### Context7 MCP
brainstorm, business-panel, cleanup, estimate, explain, implement, improve, index, spec-panel, task, workflow

### Magic MCP
brainstorm, implement, task, workflow

### Playwright MCP
brainstorm, build, implement, task, test, workflow

### Serena MCP
brainstorm, load, reflect, save, select-tool, task, workflow

### Morphllm MCP
brainstorm, select-tool, task, workflow

---

## 学习路径

### Level 1: 基础命令 (入门)
1. `/sc:help` - 了解所有命令
2. `/sc:analyze` - 代码分析
3. `/sc:document` - 文档生成
4. `/gh:gh-commit` - 智能提交

### Level 2: 工作流命令 (进阶)
1. `/sc:implement` - 功能实现
2. `/sc:test` - 测试执行
3. `/sc:improve` - 代码改进
4. `/gh:review-pr` - PR 审查

### Level 3: 编排命令 (高级)
1. `/sc:brainstorm` - 需求探索
2. `/sc:task` - 任务管理
3. `/sc:workflow` - 工作流生成
4. `/kiro:spec` - 功能规范

### Level 4: 专家命令 (专家)
1. `/sc:business-panel` - 业务分析
2. `/sc:spec-panel` - 规范审查
3. `/sc:spawn` - 任务编排
4. `/think-ultra` - 超级思考

---

## 相关资源

- [[sc-commands|SuperClaude Commands 完整指南]]
- [[gh-commands|GitHub Commands 使用指南]]
- [[../Level-3-Extension-Systems/Slash-Commands-Guide|Slash Commands 完整指南]]
- [[../Level-3-Extension-Systems/MCP-Integration|MCP Server 集成]]

---

## 总结

本项目提供了超过 112 个自定义命令,覆盖从基础开发到企业级编排的完整开发周期。

**主要特点**:
- ✅ 全面的功能覆盖
- ✅ 模块化组织结构
- ✅ 深度 MCP 集成
- ✅ 灵活的复杂度层次
- ✅ 清晰的学习路径

建议根据自己的需求和经验选择合适的命令,逐步掌握从基础到高级的使用技巧。
