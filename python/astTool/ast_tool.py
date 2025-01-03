import ast

class ASTTool:
    def __init__(self, source_code):
        """初始化，解析源代码为 AST 树"""
        self.source_code = source_code
        self.tree = ast.parse(source_code)  # 使用标准库 ast.parse 方法解析代码

    def print_ast(self):
        """打印 AST 树的结构"""
        print(ast.dump(self.tree, indent=4))

    def find_functions(self):
        """提取所有函数定义"""
        functions = []
        for node in ast.walk(self.tree):  # 遍历 AST 树
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        print(f"找到的函数: {functions}")
        return functions

    def generate_code(self):
        """生成 Python 源代码（如果修改 AST 后使用此功能）"""
        return ast.unparse(self.tree)


# 测试代码
if __name__ == "__main__":
    code = """
def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a + b
"""
    tool = ASTTool(code)

    print("AST 树结构：")
    tool.print_ast()

    print("\n提取函数名：")
    tool.find_functions()
