# C++ 函数定义指南

## 基本语法

```cpp
返回类型 函数名(参数列表) {
    // 函数体
    return 返回值;  // 可选
}
```

## 1. 基本函数定义

```cpp
// 有返回值的函数
int add(int a, int b) {
    return a + b;
}

// 无返回值的函数
void printHello() {
    cout << "Hello!" << endl;
}
```

## 2. 函数组成部分

- **返回类型**: 函数返回的数据类型（如 `int`, `double`, `void`）
- **函数名**: 标识函数的名称
- **参数列表**: 函数接收的输入参数
- **函数体**: 函数的具体实现代码
- **return语句**: 返回结果（void函数可以省略）

## 3. 常见函数类型

### 3.1 无参数函数
```cpp
void sayHello() {
    cout << "Hello, World!" << endl;
}
```

### 3.2 有参数函数
```cpp
int multiply(int a, int b) {
    return a * b;
}
```

### 3.3 默认参数函数
```cpp
void printInfo(string name, int age = 18) {
    cout << name << " is " << age << " years old" << endl;
}
```

### 3.4 函数重载
```cpp
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}
```

## 4. 函数声明 vs 函数定义

### 函数声明（原型）
```cpp
int add(int a, int b);  // 只声明，不实现
```

### 函数定义
```cpp
int add(int a, int b) {  // 声明 + 实现
    return a + b;
}
```

## 5. 函数调用

```cpp
int result = add(5, 3);  // 调用函数
printHello();            // 调用无返回值函数
```

## 6. 最佳实践

1. **函数名**: 使用有意义的名称，通常使用动词开头
2. **单一职责**: 一个函数只做一件事
3. **参数数量**: 避免过多参数（通常不超过5个）
4. **返回值**: 明确函数的返回值类型
5. **注释**: 为复杂函数添加注释说明

## 7. 编译和运行

```bash
# 编译
g++ -o function_examples src/function_examples.cpp

# 运行
./function_examples
```

## 8. 常见错误

- 忘记返回语句（非void函数）
- 参数类型不匹配
- 函数名拼写错误
- 缺少分号或大括号 