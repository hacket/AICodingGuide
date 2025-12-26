# 阿里巴巴 Android 开发规范 (Claude Code 版)

## 📋 概述

本文档基于阿里巴巴 Android 开发手册，提炼了核心规范要点，专为 Claude Code 辅助 Android 开发设计。遵循这些规范将提高代码质量、可维护性和团队协作效率。

## 🎯 核心原则

### 1. 命名规范
- **包命名**: 全小写，使用点分隔符分隔单词
  ```kotlin
  // ✅ 正确
  com.alibaba.android

  // ❌ 错误
  com.Alibaba.Android
  ```

- **类命名**: 使用 PascalCase (大驼峰)
  ```kotlin
  // ✅ 正确
  class MainActivity
  class UserManager

  // ❌ 错误
  class mainActivity
  class usermanager
  ```

- **方法和变量**: 使用 camelCase (小驼峰)
  ```kotlin
  // ✅ 正确
  fun getUserInfo()
  private val userName: String

  // ❌ 错误
  fun GetUserInfo()
  private val UserName: String
  ```

- **常量**: 全大写，下划线分隔
  ```kotlin
  // ✅ 正确
  const val MAX_PAGE_SIZE = 20
  private const val TAG = "MainActivity"

  // ❌ 错误
  const val maxPageSize = 20
  private const val tag = "MainActivity"
  ```

### 2. 代码风格

#### 缩进和空格
- 使用 4 个空格缩进，不使用 Tab
- 运算符两边添加空格
- 逗号后添加空格

```kotlin
// ✅ 正确
fun calculateSum(a: Int, b: Int): Int {
    return a + b
}

// ❌ 错误
fun calculateSum(a:Int,b:Int):Int{
return a+b
}
```

#### 大括号风格
- 使用 K&R 风格，左大括号不换行

```kotlin
// ✅ 正确
class MainActivity {
    fun onCreate() {
        // code here
    }
}

// ❌ 错误
class MainActivity
{
    fun onCreate()
    {
        // code here
    }
}
```

### 3. 资源文件规范

#### 布局文件
- 使用下划线命名法
- 按模块组织布局文件

```
res/layout/
├── activity_main.xml
├── fragment_user_profile.xml
├── item_product_list.xml
└── dialog_confirm.xml
```

#### 字符串资源
- 使用有意义的键名
- 按功能模块分组

```xml
<!-- ✅ 正确 -->
<string name="btn_confirm">确认</string>
<string name="btn_cancel">取消</string>
<string name="error_network">网络连接失败</string>

<!-- ❌ 错误 -->
<string name="button1">确认</string>
<string name="str2">取消</string>
```

#### 图片资源
- 使用描述性名称
- 按状态和用途分类

```
res/drawable/
├── ic_home_selected.png
├── ic_home_normal.png
├── bg_button_primary.xml
└── divider_horizontal.xml
```

## 🏗️ 架构规范

### 1. 包结构组织
```
com.company.app/
├── ui/                    # UI 相关
│   ├── activity/
│   ├── fragment/
│   └── adapter/
├── data/                  # 数据层
│   ├── model/
│   ├── repository/
│   └── remote/
├── domain/                # 业务逻辑层
│   ├── usecase/
│   └── repository/
├── utils/                 # 工具类
└── di/                    # 依赖注入
```

### 2. MVVM 架构模式
- **Model**: 数据模型和业务逻辑
- **View**: UI 界面和用户交互
- **ViewModel**: 连接 Model 和 View

```kotlin
// Model
data class User(
    val id: String,
    val name: String,
    val email: String
)

// ViewModel
class UserViewModel : ViewModel() {
    private val _users = MutableLiveData<List<User>>()
    val users: LiveData<List<User>> = _users

    fun loadUsers() {
        // 加载用户数据
    }
}

// View (Fragment/Activity)
class UserFragment : Fragment() {
    private val viewModel: UserViewModel by viewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewModel.users.observe(viewLifecycleOwner) { users ->
            // 更新 UI
        }
    }
}
```

## 📱 组件开发规范

### 1. Activity 规范
- 单一职责原则，一个 Activity 只负责一个主要功能
- 避免 Activity 中的业务逻辑，使用 ViewModel
- 合理使用生命周期

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.viewModel = viewModel
        binding.lifecycleOwner = this

        initViews()
        observeData()
    }

    private fun initViews() {
        // 初始化 UI
    }

    private fun observeData() {
        // 观察数据变化
    }
}
```

### 2. Fragment 规范
- 避免 Fragment 嵌套过深
- 正确处理 Fragment 生命周期
- 使用接口与 Activity/Fragment 通信

```kotlin
class UserProfileFragment : Fragment() {
    private var listener: OnUserActionListener? = null

    interface OnUserActionListener {
        fun onEditProfile(userId: String)
        fun onDeleteUser(userId: String)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is OnUserActionListener) {
            listener = context
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        listener = null
    }
}
```

### 3. Adapter 规范
- 使用 ViewHolder 模式
- 避免在 onBindViewHolder 中进行耗时操作
- 合理使用 DiffUtil

```kotlin
class UserAdapter(
    private val onItemClick: (User) -> Unit
) : ListAdapter<User, UserViewHolder>(UserDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        val binding = ItemUserBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return UserViewHolder(binding, onItemClick)
    }

    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        holder.bind(getItem(position))
    }
}

class UserViewHolder(
    private val binding: ItemUserBinding,
    private val onItemClick: (User) -> Unit
) : RecyclerView.ViewHolder(binding.root) {

    fun bind(user: User) {
        binding.userName.text = user.name
        binding.userEmail.text = user.email
        binding.root.setOnClickListener { onItemClick(user) }
    }
}
```

## 🔧 数据处理规范

### 1. 网络请求
- 使用统一的网络请求框架
- 添加错误处理和加载状态
- 合理使用缓存策略

```kotlin
class UserRepository @Inject constructor(
    private val apiService: ApiService,
    private val cache: UserCache
) {
    suspend fun getUsers(): Result<List<User>> {
        return try {
            // 先检查缓存
            cache.getUsers()?.let { cachedUsers ->
                return Result.success(cachedUsers)
            }

            // 网络请求
            val response = apiService.getUsers()
            cache.saveUsers(response.data)
            Result.success(response.data)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
```

### 2. 数据库操作
- 使用 Room 数据库
- 避免在主线程进行数据库操作
- 合理设计数据表结构

```kotlin
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    val name: String,
    val email: String,
    val createdAt: Long
)

@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY createdAt DESC")
    fun getAllUsers(): Flow<List<UserEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUsers(users: List<UserEntity>)
}
```

## 🛡️ 安全和性能规范

### 1. 内存管理
- 避免内存泄漏，正确使用生命周期
- 及时释放不需要的资源
- 合理使用图片缓存

```kotlin
class ImageLoader {
    private val memoryCache = LruCache<String, Bitmap>(4 * 1024 * 1024)

    fun loadImage(url: String, imageView: ImageView) {
        // 检查内存缓存
        memoryCache.get(url)?.let { bitmap ->
            imageView.setImageBitmap(bitmap)
            return
        }

        // 加载图片
        Glide.with(imageView.context)
            .load(url)
            .into(imageView)
    }
}
```

### 2. 线程管理
- 网络请求和数据库操作使用后台线程
- UI 更新必须在主线程
- 使用协程处理异步任务

```kotlin
class MainActivity : AppCompatActivity() {
    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 在协程中处理耗时操作
        lifecycleScope.launch {
            try {
                val data = viewModel.loadData()
                updateUI(data)
            } catch (e: Exception) {
                showError(e.message)
            }
        }
    }
}
```

### 3. 数据安全
- 敏感数据加密存储
- 使用 HTTPS 进行网络通信
- 添加数据验证和防注入

```kotlin
class SecurePreferences(context: Context) {
    private val prefs = context.getSharedPreferences("secure_prefs", Context.MODE_PRIVATE)
    private val masterKey = MasterKey.Builder(context)
        .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
        .build()

    fun saveToken(token: String) {
        val encryptedToken = encrypt(token)
        prefs.edit().putString("auth_token", encryptedToken).apply()
    }

    fun getToken(): String? {
        val encryptedToken = prefs.getString("auth_token", null) ?: return null
        return decrypt(encryptedToken)
    }
}
```

## 🧪 测试规范

### 1. 单元测试
- 为核心业务逻辑编写单元测试
- 保持测试的独立性和可重复性
- 使用 Given-When-Then 模式

```kotlin
@Test
fun `calculateTotalPrice should return correct total when items are valid`() {
    // Given
    val items = listOf(
        Item("apple", 2.0, 3),
        Item("banana", 1.5, 2)
    )
    val calculator = PriceCalculator()

    // When
    val result = calculator.calculateTotalPrice(items)

    // Then
    assertEquals(9.0, result, 0.01)
}
```

### 2. UI 测试
- 使用 Espresso 进行 UI 测试
- 测试用户交互流程
- 模拟各种用户场景

```kotlin
@Test
fun loginButton_shouldBeEnabled_when_emailAndPasswordAreValid() {
    // Given
    launchActivity<LoginActivity>()
    val emailEditText = onView(withId(R.id.et_email))
    val passwordEditText = onView(withId(R.id.et_password))
    val loginButton = onView(withId(R.id.btn_login))

    // When
    emailEditText.perform(typeText("test@example.com"))
    passwordEditText.perform(typeText("password123"))

    // Then
    loginButton.check(matches(isEnabled()))
}
```

## 📝 注释和文档规范

### 1. 类和方法注释
- 使用 KDoc 格式
- 说明功能、参数和返回值
- 提供使用示例

```kotlin
/**
 * 用户管理器，负责处理用户相关的业务逻辑
 *
 * @param userRepository 用户数据仓库
 * @param eventBus 事件总线
 */
class UserManager(
    private val userRepository: UserRepository,
    private val eventBus: EventBus
) {
    /**
     * 根据用户 ID 获取用户信息
     *
     * @param userId 用户 ID
     * @return 用户信息，如果用户不存在则返回 null
     * @throws IllegalArgumentException 当 userId 为空时抛出
     */
    suspend fun getUserById(userId: String): User? {
        require(userId.isNotBlank()) { "User ID cannot be blank" }
        return userRepository.findById(userId)
    }
}
```

### 2. 复杂逻辑注释
- 解释算法思路和实现原理
- 标注特殊情况的处理
- 提供相关参考链接

```kotlin
/**
 * 计算两个时间段的交集
 *
 * 算法思路：
 * 1. 比较两个时间段的开始时间，取较晚者作为交集开始
 * 2. 比较两个时间段的结束时间，取较早者作为交集结束
 * 3. 如果开始时间早于结束时间，则存在交集
 */
fun calculateTimeIntersection(
    start1: Long, end1: Long,
    start2: Long, end2: Long
): TimeRange? {
    val intersectionStart = maxOf(start1, start2)
    val intersectionEnd = minOf(end1, end2)

    return if (intersectionStart < intersectionEnd) {
        TimeRange(intersectionStart, intersectionEnd)
    } else {
        null // 无交集
    }
}
```

## 🔍 代码审查检查清单

### 命名和结构
- [ ] 命名是否符合规范
- [ ] 类和方法的职责是否单一
- [ ] 包结构是否合理

### 代码质量
- [ ] 是否有重复代码
- [ ] 是否有未使用的导入和变量
- [ ] 异常处理是否完善

### 性能和安全
- [ ] 是否有内存泄漏风险
- [ ] 网络请求是否在后台线程
- [ ] 敏感数据是否加密

### 测试和文档
- [ ] 是否有对应的单元测试
- [ ] 注释是否清晰完整
- [ ] 代码是否易于理解和维护

## 📚 参考资源

- [Android 官方开发指南](https://developer.android.com/guide)
- [Kotlin 编码规范](https://kotlinlang.org/docs/coding-conventions.html)
- [Jetpack Compose 指南](https://developer.android.com/jetpack/compose)
- [Android 架构指南](https://developer.android.com/jetpack/guide)

---

> 💡 **提示**: 将此文档添加到项目的 `CLAUDE.md` 或相关配置文件中，Claude Code 将会遵循这些规范为您提供 Android 开发 assistance。