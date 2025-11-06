---
title: SuperClaude (sc) Commands 完整指南
description: SuperClaude 命令组的完整使用文档
tags: [commands, sc, superclaude, workflow, automation]
created: 2025-11-04
---

# SuperClaude (sc) Commands 完整指南

SuperClaude 是一个强大的命令组,提供了 24 个专业级开发命令,涵盖代码分析、工作流管理、系统编排等多个领域。所有命令都采用 `/sc:` 前缀。

## 📋 目录

- [命令概览](#命令概览)
- [分类索引](#分类索引)
- [详细命令说明](#详细命令说明)
- [MCP Server 集成](#mcp-server-集成)

## 命令概览

| 命令 | 复杂度 | 描述 |
|------|--------|------|
| `/sc:help` | Low | 列出所有可用命令和功能 |
| `/sc:analyze` | Basic | 跨质量、安全、性能和架构的综合代码分析 |
| `/sc:build` | Enhanced | 构建、编译和打包项目,带智能错误处理 |
| `/sc:brainstorm` | Advanced | 通过苏格拉底式对话进行交互式需求探索 |
| `/sc:business-panel` | Complex | 多专家业务分析与战略规划 |
| `/sc:cleanup` | Standard | 系统化清理代码、移除死代码、优化项目结构 |
| `/sc:design` | Basic | 设计系统架构、API 和组件接口 |
| `/sc:document` | Basic | 为组件、函数、API 和功能生成文档 |
| `/sc:estimate` | Standard | 提供任务、功能或项目的开发估算 |
| `/sc:explain` | Standard | 清晰解释代码、概念和系统行为 |
| `/sc:git` | Basic | Git 操作,带智能 commit 消息生成 |
| `/sc:implement` | Standard | 功能和代码实现,带智能 Persona 激活 |
| `/sc:improve` | Standard | 系统化改进代码质量、性能和可维护性 |
| `/sc:index` | Standard | 生成综合项目文档和知识库 |
| `/sc:load` | Standard | 会话生命周期管理,加载项目上下文 |
| `/sc:reflect` | Standard | 任务反思和验证 |
| `/sc:save` | Standard | 会话上下文持久化 |
| `/sc:select-tool` | High | 基于复杂度评分的智能 MCP 工具选择 |
| `/sc:spawn` | High | 元系统任务编排,智能分解和委托 |
| `/sc:spec-panel` | Enhanced | 多专家规范审查和改进 |
| `/sc:task` | Advanced | 执行复杂任务,带智能工作流管理 |
| `/sc:test` | Enhanced | 执行测试,带覆盖率分析和质量报告 |
| `/sc:troubleshoot` | Basic | 诊断和解决代码、构建、部署中的问题 |
| `/sc:workflow` | Advanced | 从 PRD 和功能需求生成结构化实现工作流 |

## 分类索引

### 🛠️ Utility (工具类)

基础实用工具命令,用于日常开发任务。

- **analyze** - 代码分析和质量评估
- **build** - 项目构建和打包
- **design** - 架构和接口设计
- **document** - 文档生成
- **git** - Git 操作增强
- **help** - 命令帮助
- **test** - 测试执行和覆盖率
- **troubleshoot** - 问题诊断和解决

### 🔄 Workflow (工作流)

工作流优化和代码改进命令。

- **cleanup** - 代码清理和优化
- **explain** - 代码解释
- **implement** - 功能实现
- **improve** - 代码改进

### 🎭 Orchestration (编排)

高级编排命令,用于复杂任务协调。

- **brainstorm** - 需求探索和头脑风暴
- **workflow** - 工作流生成

### ⚡ Special (特殊)

特殊用途的高级命令。

- **estimate** - 开发估算
- **index** - 知识库索引
- **select-tool** - 智能工具选择
- **spawn** - 任务分解和委托
- **task** - 复杂任务管理

### 💾 Session (会话)

会话管理和上下文持久化。

- **load** - 加载项目上下文
- **reflect** - 任务反思
- **save** - 保存会话状态

### 📊 Analysis (分析)

深度分析和评审命令。

- **spec-panel** - 规范审查
- **business-panel** - 业务分析

---

## 详细命令说明

### /sc:help

**复杂度**: Low
**描述**: 列出所有可用的 /sc 命令和功能

**使用方法**:
```bash
/sc:help
```

**功能特点**:
- 显示所有可用 SuperClaude 命令的完整列表
- 提供每个命令功能的清晰描述
- 以可读的表格格式呈现信息
- 显示所有可用的 SuperClaude 框架标志

---

### /sc:analyze

**复杂度**: Basic
**类别**: Utility
**描述**: 跨质量、安全、性能和架构领域的综合代码分析

**使用方法**:
```bash
/sc:analyze [target] [--focus quality|security|performance|architecture] [--depth quick|deep] [--format text|json|report]
```

**功能特点**:
- 结合静态分析和启发式评估的多领域分析
- 智能文件发现和特定语言的模式识别
- 基于严重性的发现和建议优先级排序
- 包含指标、趋势和可行洞察的综合报告

**使用示例**:

**1. 综合项目分析**
```bash
/sc:analyze
```
整个项目的多领域分析,生成包含关键发现和路线图的综合报告。

**2. 聚焦安全评估**
```bash
/sc:analyze src/auth --focus security --depth deep
```
认证组件的深度安全分析,提供详细的修复指导。

**3. 性能优化分析**
```bash
/sc:analyze --focus performance --format report
```
性能瓶颈识别,生成包含优化建议的 HTML 报告。

**4. 快速质量检查**
```bash
/sc:analyze src/components --focus quality --depth quick
```
组件目录的快速质量评估,识别代码异味和可维护性问题。

---

### /sc:build

**复杂度**: Enhanced
**类别**: Utility
**MCP Server**: playwright
**Persona**: devops-engineer
**描述**: 构建、编译和打包项目,带智能错误处理和优化

**使用方法**:
```bash
/sc:build [target] [--type dev|prod|test] [--clean] [--optimize] [--verbose]
```

**功能特点**:
- 配置驱动的构建编排,带依赖验证
- 智能错误分析,提供可行的解决指导
- 环境特定优化 (dev/prod/test 配置)
- 包含时间指标和产物分析的综合构建报告

**使用示例**:

**1. 标准项目构建**
```bash
/sc:build
```
使用默认配置构建整个项目。

**2. 生产优化构建**
```bash
/sc:build --type prod --clean --optimize
```
清理后的生产构建,带压缩和 tree-shaking。

**3. 开发构建与验证**
```bash
/sc:build --type dev --validate
```
开发构建,集成 Playwright UI 测试。

---

### /sc:brainstorm

**复杂度**: Advanced
**类别**: Orchestration
**MCP Servers**: sequential, context7, magic, playwright, morphllm, serena
**Personas**: architect, analyzer, frontend, backend, security, devops, project-manager
**描述**: 通过苏格拉底式对话和系统化探索进行交互式需求发现

**使用方法**:
```bash
/sc:brainstorm [topic/idea] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel]
```

**功能特点**:
- 跨架构、分析、前端、后端、安全领域的多 Persona 编排
- 高级 MCP 协调,为专业分析提供智能路由
- 系统化执行,带渐进式对话增强和并行探索
- 跨会话持久化,包含综合需求发现文档

**使用示例**:

**1. 系统化产品发现**
```bash
/sc:brainstorm "AI-powered project management tool" --strategy systematic --depth deep
```
多 Persona 分析,使用 Sequential MCP 进行结构化探索。

**2. 敏捷功能探索**
```bash
/sc:brainstorm "real-time collaboration features" --strategy agile --parallel
```
并行探索,集成 Context7 和 Magic MCP。

**3. 企业解决方案验证**
```bash
/sc:brainstorm "enterprise data analytics platform" --strategy enterprise --validate
```
综合验证,使用 Serena MCP 进行跨会话持久化。

---

### /sc:business-panel

**复杂度**: Complex
**类别**: Analysis & Strategic Planning
**MCP Servers**: sequential, context7
**Personas**: analyzer, architect, mentor
**描述**: 多专家业务分析,带自适应交互模式

**使用方法**:
```bash
/sc:business-panel [document_path_or_content] [--mode discussion|debate|socratic] [--experts "name1,name2"] [--focus domain]
```

**功能特点**:
- AI 主持的知名商业思想领袖小组讨论
- 三种分析模式: Discussion (协作), Debate (对抗), Socratic (问题驱动)
- 九位专家小组,包括 Clayton Christensen, Michael Porter, Peter Drucker, Seth Godin 等
- 针对不同分析需求的自适应交互模式

**专家小组成员**:
- Clayton Christensen - 颠覆性创新理论
- Michael Porter - 竞争战略
- Peter Drucker - 管理学之父
- Seth Godin - 营销和领导力
- 以及其他 5 位知名专家

**使用示例**:

**1. 基础文档分析**
```bash
/sc:business-panel document.md
```
使用默认讨论模式进行协作分析。

**2. 辩论模式分析**
```bash
/sc:business-panel [content] --mode debate
```
通过专家辩论挑战和压力测试想法。

**3. 聚焦专家选择**
```bash
/sc:business-panel [content] --experts "porter,christensen,meadows"
```
选择特定专家进行针对性分析。

---

### /sc:cleanup

**复杂度**: Standard
**类别**: Workflow
**MCP Servers**: sequential, context7
**Personas**: architect, quality, security
**描述**: 系统化清理代码、移除死代码、优化项目结构

**使用方法**:
```bash
/sc:cleanup [target] [--type code|imports|files|all] [--safe|--aggressive] [--interactive]
```

**功能特点**:
- 基于清理类型的多 Persona 协调 (architect, quality, security)
- 通过 Context7 MCP 集成实现框架特定的清理模式
- 通过 Sequential MCP 进行复杂清理操作的系统化分析
- 安全优先方法,带备份和回滚能力

**使用示例**:

**1. 安全代码清理**
```bash
/sc:cleanup src/ --type code --safe
```
保守清理,带自动安全验证。

**2. Import 优化**
```bash
/sc:cleanup --type imports --preview
```
框架感知的未使用 import 清理预览。

**3. 综合项目清理**
```bash
/sc:cleanup --type all --interactive
```
多领域清理,为复杂决策提供用户指导。

---

### /sc:design

**复杂度**: Basic
**类别**: Utility
**描述**: 设计系统架构、API 和组件接口,生成综合规范

**使用方法**:
```bash
/sc:design [target] [--type architecture|api|component|database] [--format diagram|spec|code]
```

**功能特点**:
- 需求驱动的设计方法,考虑可扩展性
- 集成行业最佳实践,实现可维护的解决方案
- 基于需求的多格式输出 (图表、规范、代码)
- 针对现有系统架构和约束的验证

**使用示例**:

**1. 系统架构设计**
```bash
/sc:design user-management-system --type architecture --format diagram
```
创建包含组件关系的综合系统架构。

**2. API 规范设计**
```bash
/sc:design payment-api --type api --format spec
```
生成遵循 RESTful 原则的详细 API 规范。

**3. 数据库模式设计**
```bash
/sc:design e-commerce-db --type database --format diagram
```
创建包含实体关系和约束的数据库模式。

---

### /sc:document

**复杂度**: Basic
**类别**: Utility
**描述**: 为组件、函数、API 和功能生成聚焦文档

**使用方法**:
```bash
/sc:document [target] [--type inline|external|api|guide] [--style brief|detailed]
```

**功能特点**:
- 代码结构分析,带 API 提取和使用模式识别
- 多格式文档生成 (内联、外部、API 参考、指南)
- 一致的格式化和交叉引用集成
- 特定语言的文档模式和约定

**使用示例**:

**1. 内联代码文档**
```bash
/sc:document src/auth/login.js --type inline
```
生成包含综合内联文档的 JSDoc 注释。

**2. API 参考生成**
```bash
/sc:document src/api --type api --style detailed
```
创建包含使用示例的综合 API 文档。

**3. 用户指南创建**
```bash
/sc:document payment-module --type guide --style brief
```
创建包含实用示例的用户友好文档。

---

### /sc:estimate

**复杂度**: Standard
**类别**: Special
**MCP Servers**: sequential, context7
**Personas**: architect, performance, project-manager
**描述**: 提供任务、功能或项目的开发估算,带智能分析

**使用方法**:
```bash
/sc:estimate [target] [--type time|effort|complexity] [--unit hours|days|weeks] [--breakdown]
```

**功能特点**:
- 基于估算范围的多 Persona 协调 (architect, performance, project-manager)
- Sequential MCP 集成,用于系统化分析和复杂度评估
- Context7 MCP 集成,用于框架特定模式和历史基准
- 智能分解分析,带置信区间和风险因素

**使用示例**:

**1. 功能开发估算**
```bash
/sc:estimate "user authentication system" --type time --unit days --breakdown
```
系统化分解分析,85% 置信区间。

**2. 项目复杂度评估**
```bash
/sc:estimate "migrate monolith to microservices" --type complexity --breakdown
```
架构复杂度分析,带风险因素。

**3. 性能优化工作量**
```bash
/sc:estimate "optimize application performance" --type effort --unit hours
```
按优化类别的工作量分解,带预期影响。

---

### /sc:explain

**复杂度**: Standard
**类别**: Workflow
**MCP Servers**: sequential, context7
**Personas**: educator, architect, security
**描述**: 清晰解释代码、概念和系统行为,带教育性清晰度

**使用方法**:
```bash
/sc:explain [target] [--level basic|intermediate|advanced] [--format text|examples|interactive] [--context domain]
```

**功能特点**:
- 领域专业知识的多 Persona 协调 (educator, architect, security)
- 通过 Context7 集成实现框架特定解释
- 通过 Sequential MCP 进行复杂概念分解的系统化分析
- 基于受众和复杂度的自适应解释深度

**使用示例**:

**1. 基础代码解释**
```bash
/sc:explain authentication.js --level basic
```
为初学者提供清晰解释和实用示例。

**2. 框架概念解释**
```bash
/sc:explain react-hooks --level intermediate --context react
```
Context7 集成,使用官方 React 文档模式。

**3. 系统架构解释**
```bash
/sc:explain microservices-system --level advanced --format interactive
```
交互式探索,带 Sequential 分析分解。

---

### /sc:git

**复杂度**: Basic
**类别**: Utility
**描述**: Git 操作,带智能 commit 消息和工作流优化

**使用方法**:
```bash
/sc:git [operation] [args] [--smart-commit] [--interactive]
```

**功能特点**:
- 基于变更分析生成传统 commit 消息
- 应用一致的分支命名约定
- 处理合并冲突,带引导式解决
- 提供清晰的状态摘要和工作流建议

**使用示例**:

**1. 智能状态分析**
```bash
/sc:git status
```
分析仓库状态,提供可行建议。

**2. 智能 Commit**
```bash
/sc:git commit --smart-commit
```
从变更分析生成传统 commit 消息。

**3. 交互式操作**
```bash
/sc:git merge feature-branch --interactive
```
引导式合并,带冲突解决协助。

---

### /sc:implement

**复杂度**: Standard
**类别**: Workflow
**MCP Servers**: context7, sequential, magic, playwright
**Personas**: architect, frontend, backend, security, qa-specialist
**描述**: 功能和代码实现,带智能 Persona 激活和 MCP 集成

**使用方法**:
```bash
/sc:implement [feature-description] [--type component|api|service|feature] [--framework react|vue|express] [--safe] [--with-tests]
```

**功能特点**:
- 基于上下文的 Persona 激活 (architect, frontend, backend, security, qa)
- 通过 Context7 和 Magic MCP 集成实现框架特定实现
- 通过 Sequential MCP 实现系统化多组件协调
- 综合测试集成,使用 Playwright 进行验证

**使用示例**:

**1. React 组件实现**
```bash
/sc:implement user profile component --type component --framework react
```
Magic MCP 生成 UI,集成设计系统。

**2. API 服务实现**
```bash
/sc:implement user authentication API --type api --safe --with-tests
```
Backend 和 security Personas 确保最佳实践。

**3. 全栈功能**
```bash
/sc:implement payment processing system --type feature --with-tests
```
多 Persona 协调,使用 Sequential MCP 分解。

---

### /sc:improve

**复杂度**: Standard
**类别**: Workflow
**MCP Servers**: sequential, context7
**Personas**: architect, performance, quality, security
**描述**: 系统化改进代码质量、性能和可维护性

**使用方法**:
```bash
/sc:improve [target] [--type quality|performance|maintainability|style] [--safe] [--interactive]
```

**功能特点**:
- 基于改进类型的多 Persona 协调 (architect, performance, quality, security)
- 通过 Context7 集成实现框架特定优化和最佳实践
- 通过 Sequential MCP 进行复杂多组件改进的系统化分析
- 安全重构,带综合验证和回滚能力

**使用示例**:

**1. 代码质量增强**
```bash
/sc:improve src/ --type quality --safe
```
系统化质量分析,带安全重构。

**2. 性能优化**
```bash
/sc:improve api-endpoints --type performance --interactive
```
Performance Persona 分析瓶颈,带交互式指导。

**3. 安全加固**
```bash
/sc:improve auth-service --type security --validate
```
Security Persona 应用安全模式,带验证。

---

### /sc:index

**复杂度**: Standard
**类别**: Special
**MCP Servers**: sequential, context7
**Personas**: architect, scribe, quality
**描述**: 生成综合项目文档和知识库,带智能组织

**使用方法**:
```bash
/sc:index [target] [--type docs|api|structure|readme] [--format md|json|yaml]
```

**功能特点**:
- 基于文档范围的多 Persona 协调 (architect, scribe, quality)
- Sequential MCP 集成,用于系统化分析和综合文档
- Context7 MCP 集成,用于框架特定模式和文档标准
- 智能组织,带交叉引用和自动化维护

**使用示例**:

**1. 项目结构文档**
```bash
/sc:index project-root --type structure --format md
```
综合项目结构,带交叉引用。

**2. API 文档生成**
```bash
/sc:index src/api --type api --format json
```
API 文档,带系统化分析和验证。

**3. 知识库创建**
```bash
/sc:index . --type docs
```
交互式知识库,带项目特定模式。

---

### /sc:load

**复杂度**: Standard
**类别**: Session
**MCP Server**: serena
**描述**: 会话生命周期管理,使用 Serena MCP 集成加载项目上下文

**使用方法**:
```bash
/sc:load [target] [--type project|config|deps|checkpoint] [--refresh] [--analyze]
```

**功能特点**:
- Serena MCP 集成,用于内存管理和跨会话持久化
- 项目激活,带综合上下文加载和验证
- 性能关键操作,目标初始化时间 <500ms
- 会话生命周期管理,带检查点和内存协调

**使用示例**:

**1. 基础项目加载**
```bash
/sc:load
```
加载当前目录,集成 Serena 内存。

**2. 特定项目加载**
```bash
/sc:load /path/to/project --type project --analyze
```
加载特定项目,带综合分析。

**3. 检查点恢复**
```bash
/sc:load --type checkpoint --checkpoint session_123
```
恢复特定检查点,完整保留上下文。

---

### /sc:reflect

**复杂度**: Standard
**类别**: Session
**MCP Server**: serena
**描述**: 任务反思和验证,使用 Serena MCP 分析能力

**使用方法**:
```bash
/sc:reflect [--type task|session|completion] [--analyze] [--validate]
```

**功能特点**:
- Serena MCP 集成,用于综合反思分析和任务验证
- TodoWrite 模式与高级 Serena 分析能力之间的桥梁
- 会话生命周期集成,带跨会话持久化和学习捕获
- 性能关键操作,核心反思和验证 <200ms

**使用示例**:

**1. 任务遵循反思**
```bash
/sc:reflect --type task --analyze
```
验证当前方法是否符合项目目标。

**2. 会话进度分析**
```bash
/sc:reflect --type session --validate
```
综合分析会话工作和质量。

**3. 完成验证**
```bash
/sc:reflect --type completion
```
评估任务完成标准和剩余工作。

---

### /sc:save

**复杂度**: Standard
**类别**: Session
**MCP Server**: serena
**描述**: 会话生命周期管理,使用 Serena MCP 集成进行会话上下文持久化

**使用方法**:
```bash
/sc:save [--type session|learnings|context|all] [--summarize] [--checkpoint]
```

**功能特点**:
- Serena MCP 集成,用于内存管理和跨会话持久化
- 基于会话进度和关键任务的自动检查点创建
- 会话上下文保留,带综合发现和模式归档
- 跨会话学习,带累积项目洞察和技术决策

**使用示例**:

**1. 基础会话保存**
```bash
/sc:save
```
将当前会话发现保存到 Serena MCP。

**2. 综合会话检查点**
```bash
/sc:save --type all --checkpoint
```
完整会话保留,带恢复检查点。

**3. 会话摘要生成**
```bash
/sc:save --summarize
```
创建会话摘要,带发现文档。

---

### /sc:select-tool

**复杂度**: High
**类别**: Special
**MCP Servers**: serena, morphllm
**描述**: 基于复杂度评分和操作分析的智能 MCP 工具选择

**使用方法**:
```bash
/sc:select-tool [operation] [--analyze] [--explain]
```

**功能特点**:
- 基于文件数量、操作类型、语言和框架的复杂度评分
- 性能评估,评估速度与准确性权衡
- 决策逻辑矩阵,带直接映射和基于阈值的路由
- Serena (语义) vs Morphllm (模式) 操作的工具能力匹配

**使用示例**:

**1. 复杂重构操作**
```bash
/sc:select-tool "rename function across 10 files" --analyze
```
高复杂度分析选择 Serena MCP 的 LSP 能力。

**2. 基于模式的批量编辑**
```bash
/sc:select-tool "update console.log to logger.info across project" --explain
```
模式转换选择 Morphllm 以提高速度。

**3. 内存管理操作**
```bash
/sc:select-tool "save project context and discoveries"
```
直接映射到 Serena MCP 用于项目上下文。

---

### /sc:spawn

**复杂度**: High
**类别**: Special
**描述**: 元系统任务编排,带智能分解和委托

**使用方法**:
```bash
/sc:spawn [complex-task] [--strategy sequential|parallel|adaptive] [--depth normal|deep]
```

**功能特点**:
- 元系统任务分解,带 Epic → Story → Task → Subtask 分解
- 基于操作特征的智能协调策略选择
- 跨领域操作管理,带并行和顺序执行
- 跨任务层次的高级依赖分析和资源优化

**使用示例**:

**1. 复杂功能实现**
```bash
/sc:spawn "implement user authentication system"
```
跨数据库、后端、前端、测试领域的分解。

**2. 大规模系统操作**
```bash
/sc:spawn "migrate legacy monolith to microservices" --strategy adaptive --depth deep
```
企业级操作,带复杂编排。

**3. 跨领域基础设施**
```bash
/sc:spawn "establish CI/CD pipeline with security scanning"
```
跨 DevOps、Security、Quality 领域的系统级操作。

---

### /sc:spec-panel

**复杂度**: Enhanced
**类别**: Analysis
**MCP Servers**: sequential, context7
**Personas**: technical-writer, system-architect, quality-engineer
**描述**: 多专家规范审查和改进,使用知名规范和软件工程专家

**使用方法**:
```bash
/sc:spec-panel [specification_content|@file] [--mode discussion|critique|socratic] [--experts "name1,name2"] [--focus requirements|architecture|testing|compliance]
```

**功能特点**:
- 多专家视角分析,带不同方法论和质量框架
- 基于规范领域和焦点的智能专家选择
- 结构化审查流程,带基于证据的建议
- 迭代改进周期,带质量验证和进度跟踪
- 专家小组包括 Karl Wiegers, Gojko Adzic, Martin Fowler, Michael Nygard 等

**使用示例**:

**1. API 规范审查**
```bash
/sc:spec-panel @auth_api.spec.yml --mode critique --focus requirements,architecture
```
综合 API 规范审查,带改进建议。

**2. 需求研讨会**
```bash
/sc:spec-panel "user story content" --mode discussion --experts "wiegers,adzic,cockburn"
```
协作需求分析和细化。

**3. 迭代改进**
```bash
/sc:spec-panel @complex_system.spec.yml --iterations 3 --format detailed
```
多次迭代改进,带专家指导。

---

### /sc:task

**复杂度**: Advanced
**类别**: Special
**MCP Servers**: sequential, context7, magic, playwright, morphllm, serena
**Personas**: architect, analyzer, frontend, backend, security, devops, project-manager
**描述**: 执行复杂任务,带智能工作流管理和委托

**使用方法**:
```bash
/sc:task [action] [target] [--strategy systematic|agile|enterprise] [--parallel] [--delegate]
```

**功能特点**:
- 跨 architect, frontend, backend, security, devops 领域的多 Persona 协调
- 智能 MCP 服务器路由 (Sequential, Context7, Magic, Playwright, Morphllm, Serena)
- 系统化执行,带渐进式任务增强和跨会话持久化
- 高级任务委托,带层次分解和依赖管理

**使用示例**:

**1. 复杂功能开发**
```bash
/sc:task create "enterprise authentication system" --strategy systematic --parallel
```
综合任务分解,带多领域协调。

**2. 敏捷 Sprint 协调**
```bash
/sc:task execute "feature backlog" --strategy agile --delegate
```
迭代执行,带跨会话持久化。

**3. 多领域集成**
```bash
/sc:task execute "microservices platform" --strategy enterprise --parallel
```
企业级协调,带合规验证。

---

### /sc:test

**复杂度**: Enhanced
**类别**: Utility
**MCP Server**: playwright
**Persona**: qa-specialist
**描述**: 执行测试,带覆盖率分析和自动化质量报告

**使用方法**:
```bash
/sc:test [target] [--type unit|integration|e2e|all] [--coverage] [--watch] [--fix]
```

**功能特点**:
- 自动检测测试框架和配置
- 生成包含指标的综合覆盖率报告
- 激活 Playwright MCP 进行 e2e 浏览器测试
- 提供智能测试失败分析
- 支持开发的连续监视模式

**使用示例**:

**1. 基础测试执行**
```bash
/sc:test
```
发现并运行所有测试,带覆盖率摘要。

**2. 针对性覆盖率分析**
```bash
/sc:test src/components --type unit --coverage
```
单元测试,带详细覆盖率指标。

**3. 浏览器测试**
```bash
/sc:test --type e2e
```
激活 Playwright 进行跨浏览器测试。

---

### /sc:troubleshoot

**复杂度**: Basic
**类别**: Utility
**描述**: 诊断和解决代码、构建、部署和系统行为中的问题

**使用方法**:
```bash
/sc:troubleshoot [issue] [--type bug|build|performance|deployment] [--trace] [--fix]
```

**功能特点**:
- 系统化根因分析,带假设测试
- 多领域故障排除 (代码、构建、性能、部署)
- 结构化调试方法论,带综合问题分析
- 安全修复应用,带验证和文档

**使用示例**:

**1. 代码 Bug 调查**
```bash
/sc:troubleshoot "Null pointer exception in user service" --type bug --trace
```
系统化分析,带针对性修复建议。

**2. 构建失败分析**
```bash
/sc:troubleshoot "TypeScript compilation errors" --type build --fix
```
分析构建日志并应用安全修复。

**3. 性能问题诊断**
```bash
/sc:troubleshoot "API response times degraded" --type performance
```
性能指标分析,带优化建议。

---

### /sc:workflow

**复杂度**: Advanced
**类别**: Orchestration
**MCP Servers**: sequential, context7, magic, playwright, morphllm, serena
**Personas**: architect, analyzer, frontend, backend, security, devops, project-manager
**描述**: 从 PRD 和功能需求生成结构化实现工作流

**使用方法**:
```bash
/sc:workflow [prd-file|feature-description] [--strategy systematic|agile|enterprise] [--depth shallow|normal|deep] [--parallel]
```

**功能特点**:
- 跨架构、前端、后端、安全、devops 领域的多 Persona 编排
- 高级 MCP 协调,为专业工作流分析提供智能路由
- 系统化执行,带渐进式工作流增强和并行处理
- 跨会话工作流管理,带综合依赖跟踪

**使用示例**:

**1. 系统化 PRD 工作流**
```bash
/sc:workflow ClaudeDocs/PRD/feature-spec.md --strategy systematic --depth deep
```
综合 PRD 分析,带多 Persona 协调。

**2. 敏捷功能工作流**
```bash
/sc:workflow "user authentication system" --strategy agile --parallel
```
敏捷工作流,集成 Context7 和 Magic MCP。

**3. 企业实现规划**
```bash
/sc:workflow enterprise-prd.md --strategy enterprise --validate
```
企业级工作流,带合规验证。

---

## MCP Server 集成

SuperClaude 命令广泛集成了多个 MCP Server,以提供增强的功能:

### Sequential MCP
**使用命令** (10): brainstorm, cleanup, estimate, explain, implement, improve, index, spec-panel, task, workflow

**功能**: 系统化分析、结构化探索、复杂概念分解

### Context7 MCP
**使用命令** (11): brainstorm, business-panel, cleanup, estimate, explain, implement, improve, index, spec-panel, task, workflow

**功能**: 框架特定模式、官方文档集成、最佳实践

### Magic MCP
**使用命令** (5): brainstorm, implement, task, workflow

**功能**: UI 组件生成、设计系统集成

### Playwright MCP
**使用命令** (6): brainstorm, build, implement, task, test, workflow

**功能**: E2E 浏览器测试、UI 验证

### Morphllm MCP
**使用命令** (4): brainstorm, select-tool, task, workflow

**功能**: 快速模式转换、批量编辑

### Serena MCP
**使用命令** (7): brainstorm, load, reflect, save, select-tool, task, workflow

**功能**: 内存管理、跨会话持久化、项目上下文

---

## 学习资源

- [[Level-3-Extension-Systems/Slash-Commands-Guide|Slash Commands 完整指南]]
- [[Level-3-Extension-Systems/MCP-Integration|MCP Server 集成]]
- [[Level-3-Extension-Systems/Sub-Agents|Sub Agents 系统]]

---

## 总结

SuperClaude (sc) 命令组提供了从基础工具到高级编排的完整开发工作流支持。通过合理组合使用这些命令,可以显著提升开发效率和代码质量。

建议按照复杂度逐步学习:
1. **入门**: help, analyze, git, document
2. **进阶**: implement, improve, test, troubleshoot
3. **高级**: brainstorm, task, workflow, spawn
4. **专家**: business-panel, spec-panel, select-tool
