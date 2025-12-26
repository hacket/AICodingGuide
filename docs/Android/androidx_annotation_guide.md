# AndroidX Annotation 使用规范 (Kotlin)

## 注解速查表

### 1. 空值注解（Kotlin 可选）
Kotlin 已有空安全，仅在 Java 互操作时使用：
```kotlin
// Kotlin 调用 Java 时有用
fun javaApi(user: User) { }  // 编译器会识别 Java 的 @NonNull
```

### 2. 资源注解
```kotlin
fun setLayout(@LayoutRes layoutId: Int) { }
fun setIcon(@DrawableRes iconRes: Int) { }
fun setText(@StringRes stringRes: Int) { }
fun setColor(@ColorRes colorRes: Int) { }
```

### 3. 线程注解
```kotlin
@UiThread
fun updateUI() { }

@WorkerThread
fun loadData(): Bitmap { }
```

### 4. 数值范围注解
```kotlin
fun setAlpha(@IntRange(from = 0, to = 255) alpha: Int) { }
fun setProgress(@FloatRange(from = 0.0, to = 1.0) progress: Float) { }
fun setColor(@ColorInt color: Int) { }  // ARGB
fun setPadding(@Px padding: Int) { }
```

### 5. 类型定义注解（替代 enum）
```kotlin
@Retention(AnnotationRetention.SOURCE)
@IntDef(STATE_IDLE, STATE_PLAYING, STATE_PAUSED)
annotation class State

const val STATE_IDLE = 0
const val STATE_PLAYING = 1
const val STATE_PAUSED = 2

fun setState(@State state: Int) { }
```

### 6. 其他常用注解
```kotlin
@Keep  // 防止混淆
data class Model(val name: String)

@RequiresApi(Build.VERSION_CODES.O)
fun useAndroidO() { }

@RequiresPermission(Manifest.permission.CAMERA)
fun openCamera() { }

@CallSuper
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
}
```

## Kotlin 使用建议

1. **空值注解**：Kotlin 已有空安全，无需 `@NonNull`/`@Nullable`
2. **资源注解**：必须使用（`@LayoutRes`, `@DrawableRes` 等）
3. **线程注解**：必须使用（`@UiThread`, `@WorkerThread`）
4. **范围注解**：必须使用（`@IntRange`, `@FloatRange`）
5. **常量定义**：优先 `@IntDef`，次选 `enum class`，最后 `sealed class`
6. **Keep 注解**：数据类（data class）用于序列化时必须加 `@Keep`

## 性能对比

| 方式 | 内存开销 | 适用场景 |
|-----|---------|---------|
| `@IntDef` | 零开销 | 简单常量 |
| `enum class` | 有开销 | 需要方法 |
| `sealed class` | 中等 | 复杂状态 |
