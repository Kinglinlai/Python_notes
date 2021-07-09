# 写在前面

这是 我 个人在学习 <i>python</i> 的学习笔记



# 计划学习书目

* 《Python编程从入门到实践》
* 《流畅的python》

<i>Updated 2021/6/23 Jun 23</i>

<i>Chapter ended 2021/7/8 Jul 8</i>

## 2. 变量和简单数据类型

1. 解释器，确定程序含义；语法高亮，突出显示程序成分

   <hr>

2. 变量

   `message = "Hello World!"`

   **注意小心拼写&命名**

   <hr>

3. 字符串

   * 单双引号都可：

     `"This is a string"`

     `'This is another string'`

   * `STRING.title()`

     将所有单词首字符大写

     ```python
     content = "this is a title"
     print(content.title())
     ```

     > This Is A Title

   * `SRTING.upper()` or `STRING.lower()`

     将所有字符大写、小写

   * 格式化`f`

     ```python
     variable_A = ...
     varaible_B = ...
     mainString = f"...{variable_A}...{variable_B} ..."
     ```

     > mainString => ...(What in A)...(What in B)...

   * 制表符`\t`换行符`\n`

   * `STRING.strip()`

     删除两侧空白

   * `STRING.lstrip()`or`STRING.rstrip()`

     删除左侧、右侧空白

     <hr>

4. 数

   * `+` `-` `*` `/` 

     ```python
     1 + 1 #2
     2 - 1 #1
     3 * 2 #6
     6 / 4 #1.5
     3 ** 2 #9
     
     ```

   * 整数`x`浮点数`x.xxxx`

   * 下划线  **python3.6+only**

     ```python
     largeNumber = 10_000_000_000_000
     print(largeNumber)
     ```

     > 10000000000000

   * 同时赋值

     ```
     x, y, z = 0,0,0
     ```

   * 常量 **记得大写**

     ```
     CONSTANT = 1145
     ```

   <hr>

5. 注释

   * 注释

     ```
     # Hahaha this is just a coment
     a = 1 + 1
     print(a)
     ```

     > 2

     解释器忽略了第一行

     

