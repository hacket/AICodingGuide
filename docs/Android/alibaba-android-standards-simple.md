# 阿里巴巴 Android 开发规范 (简化版)

## 📋 核心原则

### 1. 命名规范
```kotlin
// 包名：全小写，点分隔
com.company.app

// 类名：大驼峰
class MainActivity

// 方法/变量：小驼峰
fun getUserInfo()
private val userName: String

// 常量：全大写，下划线
const val MAX_SIZE = 20
```

### 2. 代码风格
- 使用 4 个空格缩进
- 运算符两边加空格
- 左大括号不换行

```kotlin
fun calculateSum(a: Int, b: Int): Int {
    return a + b
}
```

## 🏗️ 架构规范

### MVVM 模式
```
Model: 数据和业务逻辑
View: UI界面
ViewModel: 连接Model和View
```

### 包结构
```
com.company.app/
├── ui/          # UI相关
├── data/        # 数据层
├── domain/      # 业务逻辑
└── utils/       # 工具类
```

## 📱 组件规范

### Activity
- 单一职责，避免业务逻辑
- 使用ViewModel管理数据
- 正确处理生命周期

```kotlin
class MainActivity : AppCompatActivity() {
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 初始化UI，观察数据
    }
}
```

### Fragment
- 避免深层嵌套
- 正确处理生命周期
- 使用接口通信

### Adapter
- 使用ViewHolder模式
- 避免onBindViewHolder耗时操作
- 使用DiffUtil优化列表

## 🔧 数据处理

### 网络请求
- 使用统一框架
- 添加错误处理
- 合理使用缓存

```kotlin
suspend fun loadUsers(): Result<List<User>> {
    return try {
        val response = apiService.getUsers()
        Result.success(response.data)
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```

### 数据库
- 使用Room数据库
- 避免主线程操作
- 合理设计表结构

## 🛡️ 安全和性能

### 内存管理
- 避免内存泄漏
- 及时释放资源
- 合理使用图片缓存

### 线程管理
- 网络请求使用后台线程
- UI更新在主线程
- 使用协程处理异步任务

```kotlin
lifecycleScope.launch {
    val data = viewModel.loadData()
    updateUI(data)
}
```

### 数据安全
- 敏感数据加密
- 使用HTTPS通信
- 添加数据验证

## 🧪 测试规范

### 单元测试
- 为核心逻辑编写测试
- 使用Given-When-Then模式

```kotlin
@Test
fun calculateTotal_should_returnCorrectResult() {
    // Given
    val items = listOf(Item("apple", 2.0, 3))

    // When
    val result = calculator.calculateTotal(items)

    // Then
    assertEquals(6.0, result)
}
```

### UI测试
- 使用Espresso测试UI
- 测试用户交互流程

## 📝 注释规范

```kotlin
/**
 * 用户管理器
 *
 * @param repo 用户数据仓库
 */
class UserManager(private val repo: UserRepository) {

    /**
     * 根据ID获取用户
     * @param userId 用户ID
     * @return 用户信息
     */
    suspend fun getUserById(userId: String): User?
}
```

## ✅ 代码审查清单

### 命名和结构
- [ ] 命名符合规范
- [ ] 职责单一
- [ ] 结构合理

### 代码质量
- [ ] 无重复代码
- [ ] 无未使用代码
- [ ] 异常处理完善

### 性能和安全
- [ ] 无内存泄漏
- [ ] 后台线程处理耗时操作
- [ ] 敏感数据加密

### 测试和文档
- [ ] 有单元测试
- [ ] 注释清晰
- [ ] 代码易维护

---

> 💡 将此规范配置到Claude Code中，获得符合阿里标准的Android开发辅助。