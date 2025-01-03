# Python AST 工具

## 项目介绍
这是一个 Python 工具集合，用于操作、分析和可视化抽象语法树（AST）。

主要功能：
1. **AST 解析**：解析 Python 源代码为抽象语法树。
2. **AST 分析**：提取函数定义、变量和语法结构。
3. **AST 修改**：支持对 AST 进行修改，并生成新的代码。
4. **AST 可视化**：以图形化方式展示代码结构。

---

## 文件说明

### 1. `ast_tool.py`
- 解析和分析 AST。
- 功能包括：
    - 打印 AST 树。
    - 提取函数定义。
    - 修改并生成代码。

### 2. `visualize.py`
- 可视化 AST 结构，生成图片。
- 使用 `graphviz` 将 AST 转换为图形化表示。

### 3. `__init__.py`
- 将文件夹标记为 Python 包。

---

## 安装依赖

使用以下命令安装必要依赖：
```bash
pip install astpretty graphviz
