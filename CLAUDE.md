# CLAUDE.md

这个文件给 Claude Code 提供项目开发指导。

## 项目概述

这是一个中文 AI 编程知识库，包含两大部分：

1. **ClaudeCode** - Claude Code 完整学习指南（安装、配置、命令、技巧）
2. **Prompt Engineering** - 实用 Prompt 示例集（角色扮演、学习、开发、写作等）

## 目录结构

```
AICodingTips/
├── ClaudeCode/              # Claude Code 学习指南
│   ├── 01-Core/            # 核心功能：安装、命令、配置
│   ├── 02-Extensions/      # 扩展系统：MCP、Hooks、Skills
│   ├── 03-Best-Practices/  # 最佳实践和技巧
│   ├── COMMANDS.md         # 120+ 命令速查
│   ├── SKILLS.md           # 19 个技能说明
│   └── README.md           # 导航入口
│
├── Prompt Engineering/      # Prompt 示例库
│   ├── Role/               # 角色扮演类 (3 个)
│   ├── Plan/               # 规划思考类 (1 个)
│   ├── 开发/                # 代码开发类 (7 个)
│   ├── 学习/                # 学习教育类 (9 个)
│   ├── 写作/                # 写作辅助类 (3 个)
│   ├── 翻译/                # 翻译类 (2 个)
│   ├── AI/                 # AI 分析类 (2 个)
│   ├── 其他/                # 其他工具 (3 个)
│   └── README.md           # 导航和使用指南
│
├── docs/                   # 参考文档
│   ├── Android/           # Android 开发规范和手册
│   ├── CLAUDE.md/         # 开发准则
│   └── commands/          # 命令文档
│
└── README.md              # 项目总导航
```

## 开发原则

### 语言和术语
- 主要使用简体中文
- 技术术语保留英文：Android、Kotlin、Java、Python、Git、Claude Code、MCP、Hooks 等
- 不使用"AI 味道"很重的表达，保持人性化和简洁

### 文档编写
- 不使用 YAML frontmatter
- 使用相对路径进行内部链接
- 避免重复内容，保持逻辑关联
- 每个文档控制在合理长度，过长需拆分
- 简洁详细，不要废话

### 目录组织
- 每个目录下文件数量控制在 8 个以内
- 超过 8 个需创建子目录分类
- 保持目录结构简洁清晰

## Android 开发规范

项目包含完整的 Android 编码规范（基于阿里巴巴标准）：
- **主文档**：`ClaudeCode/01-Core/07-Android编码规范.md`
- **参考资源**：`docs/Android/` 目录下的详细文档和 PDF

在为 Android 项目提供开发建议时，优先参考这些规范。

## 项目特色

专为中文开发者打造的 AI 编程学习资源，内容实用、结构清晰、持续更新。
