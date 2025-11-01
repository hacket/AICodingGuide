# 🧪 Webapp Testing - Web 应用测试工具包

## 概述

使用 Playwright 与本地 Web 应用交互和测试，验证前端功能、调试 UI 行为、捕获截图。

**适用场景**：
- 前端功能测试
- UI 自动化
- 截图和记录
- 调试和问题定位

---

## 🎯 核心功能

### 1. 浏览器自动化
- ✅ 页面导航
- ✅ 元素交互
- ✅ 表单填写
- ✅ 点击和输入

### 2. 测试验证
- ✅ 元素存在性
- ✅ 文本内容检查
- ✅ 样式验证
- ✅ 行为测试

### 3. 调试工具
- ✅ 截图捕获
- ✅ 控制台日志
- ✅ 网络请求
- ✅ 元素检查

### 4. 高级功能
- ✅ 等待和同步
- ✅ 多标签页
- ✅ 文件上传
- ✅ 对话框处理

---

## 🔧 使用方法

### 场景 1: 测试登录功能

**示例需求**：
```
测试本地应用的登录流程
```

**步骤**：
```javascript
// 打开登录页
await page.goto('http://localhost:3000/login');

// 填写表单
await page.fill('input[name="email"]', 'user@example.com');
await page.fill('input[name="password"]', 'password123');

// 点击登录
await page.click('button[type="submit"]');

// 验证跳转
await expect(page).toHaveURL('http://localhost:3000/dashboard');
```

---

### 场景 2: 捕获页面截图

**示例需求**：
```
捕获应用不同状态的截图
```

**用途**：
- Bug 报告
- 视觉回归测试
- 文档截图
- UI 审查

---

### 场景 3: 验证数据加载

**示例需求**：
```
验证数据表格正确加载和显示
```

**检查**：
- 表格元素存在
- 数据行数正确
- 排序功能工作
- 筛选功能正常

---

## 💡 核心价值

- 🤖 **自动化** - 重复测试自动执行
- 🐛 **调试** - 快速定位问题
- 📸 **可视化** - 截图和录制
- ✅ **验证** - 确保功能正常

---

## 🚀 快速开始

```
测试我的本地应用登录功能
捕获首页截图
验证表单提交是否正常
检查响应式布局
```

---

## 📖 相关资源

- `.claude/skills/webapp-testing/SKILL.md`
- [Playwright 文档](https://playwright.dev/)
- [测试最佳实践](https://playwright.dev/docs/best-practices)

---

**记住：Webapp Testing 让前端测试自动化、可视化！** 🧪✨
