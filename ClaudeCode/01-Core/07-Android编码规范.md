# Android 编码规范

基于阿里巴巴 Android 开发手册整理，专为 Claude Code 辅助开发使用。

## 命名规范

### 包名
全小写，点分隔：
```kotlin
com.company.app  // ✅
com.Company.App  // ❌
```

### 类名
大驼峰（PascalCase）：
```kotlin
class MainActivity        // ✅
class UserManager        // ✅
class mainActivity       // ❌
```

### 方法和变量
小驼峰（camelCase）：
```kotlin
fun getUserInfo()              // ✅
private val userName: String   // ✅
fun GetUserInfo()             // ❌
```

### 常量
全大写，下划线分隔：
```kotlin
const val MAX_PAGE_SIZE = 20      // ✅
private const val TAG = "Main"    // ✅
const val maxPageSize = 20        // ❌
```

---

## 代码风格

### 格式化
- 4 个空格缩进
- 运算符两边加空格
- 左大括号不换行

```kotlin
fun calculateSum(a: Int, b: Int): Int {
    return a + b
}
```

### 注释
对复杂逻辑添加注释：
```kotlin
/**
 * 用户管理器
 * @param repo 用户数据仓库
 */
class UserManager(private val repo: UserRepository) {
    /**
     * 根据ID获取用户
     * @param userId 用户ID
     * @return 用户信息，不存在返回null
     */
    suspend fun getUserById(userId: String): User?
}
```

---

## 架构规范

### MVVM 模式
```
Model      - 数据和业务逻辑
View       - UI界面
ViewModel  - 连接Model和View
```

### 包结构
```
com.company.app/
├── ui/          # Activity、Fragment、自定义View
├── data/        # 数据层：Repository、数据源
├── domain/      # 业务逻辑：UseCase
└── utils/       # 工具类
```

---

## 组件规范

### Activity
单一职责，避免业务逻辑：
```kotlin
class MainActivity : AppCompatActivity() {
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        observeData()
    }

    private fun observeData() {
        viewModel.users.observe(this) { users ->
            updateUserList(users)
        }
    }
}
```

### Fragment
- 避免深层嵌套
- 使用接口与Activity通信
- 正确处理生命周期

### Adapter
使用ViewHolder + DiffUtil：
```kotlin
class UserAdapter : ListAdapter<User, UserViewHolder>(UserDiffCallback()) {
    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        holder.bind(getItem(position))
    }
}

class UserDiffCallback : DiffUtil.ItemCallback<User>() {
    override fun areItemsTheSame(old: User, new: User) = old.id == new.id
    override fun areContentsTheSame(old: User, new: User) = old == new
}
```

---

## 数据处理

### 网络请求
使用协程处理异步，添加错误处理：
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
使用Room，后台线程操作：
```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM user")
    suspend fun getAllUsers(): List<User>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: User)
}
```

---

## AndroidX 注解规范

### 资源注解
必须使用，IDE会进行类型检查：
```kotlin
fun setLayout(@LayoutRes layoutId: Int)
fun setIcon(@DrawableRes iconRes: Int)
fun setText(@StringRes stringRes: Int)
fun setColor(@ColorRes colorRes: Int)
```

### 线程注解
标明方法运行的线程：
```kotlin
@UiThread
fun updateUI() {
    // 必须在主线程调用
}

@WorkerThread
fun loadData(): Bitmap {
    // 必须在后台线程调用
}
```

### 数值范围注解
限制参数取值范围：
```kotlin
fun setAlpha(@IntRange(from = 0, to = 255) alpha: Int)
fun setProgress(@FloatRange(from = 0.0, to = 1.0) progress: Float)
fun setColor(@ColorInt color: Int)  // ARGB格式
fun setPadding(@Px padding: Int)     // 像素值
```

### IntDef 替代 Enum
性能更好，零内存开销：
```kotlin
@Retention(AnnotationRetention.SOURCE)
@IntDef(STATE_IDLE, STATE_PLAYING, STATE_PAUSED)
annotation class State

const val STATE_IDLE = 0
const val STATE_PLAYING = 1
const val STATE_PAUSED = 2

fun setState(@State state: Int) { }
```

### 其他常用注解
```kotlin
@Keep  // 防止混淆，用于序列化的数据类
data class User(val name: String)

@RequiresApi(Build.VERSION_CODES.O)
fun useAndroidO() { }

@RequiresPermission(Manifest.permission.CAMERA)
fun openCamera() { }

@CallSuper
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
}
```

---

## 性能和安全

### 内存管理
- 避免内存泄漏：及时取消订阅、移除监听器
- 使用 `lifecycleScope` 管理协程
- 图片使用 Glide/Coil 等框架

### 线程管理
```kotlin
lifecycleScope.launch {
    // 在协程中执行后台任务
    val data = withContext(Dispatchers.IO) {
        loadDataFromNetwork()
    }
    // 自动切回主线程更新UI
    updateUI(data)
}
```

### 数据安全
- 敏感数据加密存储
- 使用HTTPS通信
- API密钥不要硬编码

---

## 测试规范

### 单元测试
使用Given-When-Then模式：
```kotlin
@Test
fun calculateTotal_withValidItems_returnsCorrectTotal() {
    // Given
    val items = listOf(Item("apple", 2.0, 3))

    // When
    val result = calculator.calculateTotal(items)

    // Then
    assertEquals(6.0, result)
}
```

### UI测试
使用Espresso测试用户交互：
```kotlin
@Test
fun clickButton_shouldShowToast() {
    onView(withId(R.id.button)).perform(click())
    onView(withText("Success")).inRoot(isToast()).check(matches(isDisplayed()))
}
```

---

## Code Review 检查清单

### 命名和结构
- [ ] 命名符合规范（包、类、方法、变量、常量）
- [ ] 类职责单一
- [ ] 包结构合理

### 代码质量
- [ ] 无重复代码
- [ ] 无未使用的代码
- [ ] 异常处理完善
- [ ] 添加了必要的注解（资源、线程、范围等）

### 性能和安全
- [ ] 无内存泄漏（协程、监听器、订阅）
- [ ] 耗时操作在后台线程
- [ ] 敏感数据已加密
- [ ] 使用HTTPS

### 测试和文档
- [ ] 核心逻辑有单元测试
- [ ] 复杂逻辑有注释
- [ ] 代码易于维护

---

## 参考资源

- [阿里巴巴 Android 开发手册](../../../docs/Android/阿里巴巴Android%20开发手册.pdf)
- [详细开发规范](../../../instructions/alibaba-android-development-standards.md)
- [AndroidX 注解指南](../../../instructions/androidx_annotation_guide.md)

---

> 💡 将此规范配置到 Claude Code 的 CLAUDE.md 中，即可获得符合规范的 Android 开发辅助。
