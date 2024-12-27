import inspect
import importlib

def count_classes_in_module(module_name):
    module = importlib.import_module(module_name)
    class_count = 0

    # 遍历模块中的所有对象
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            class_count += 1
            print(f"Class: {name}")

    return class_count

module_name = 'openpyxl.cell'  # 替换为你要查询的模块名
class_count = count_classes_in_module(module_name)
print(f"Total number of classes in module '{module_name}': {class_count}")