import inspect
import importlib

def count_functions_in_module(module_name):
    module = importlib.import_module(module_name)
    function_count = 0

    # 遍历模块中的所有对象
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            function_count += 1
            print(f"Function: {name}")

    return function_count

module_name = 'openpyxl'  # 替换为你要查询的模块名
function_count = count_functions_in_module(module_name)
print(f"Total number of functions in module '{module_name}': {function_count}")