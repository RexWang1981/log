print("Method #1")
import openpyxl  # 替换为你要查询的模块
help(openpyxl.Workbook)  # 替换为你要查询的函数
print("-----------------------我是分割线-----------------------")
print("Method #2")
print(openpyxl.workbook.__doc__)  # 替换为你要查询的函数 函数通常有一个文档字符串，可以通过 .__doc__ 属性访问：
print("-----------------------我是分割线-----------------------")
print("Method #3")

import inspect
source_code = inspect.getsource(openpyxl.workbook)  # 替换为你要查询的函数
print(source_code)

"""
help(): 提供函数的文档字符串及其用法。
.__doc__: 直接访问函数的文档字符串。
IDE/编辑器: 使用编辑器的功能查看函数的文档。
inspect.getsource(): 查看函数的源代码（如果可用）。
这些方法可以帮助你获取函数的用法和详细信息。
"""