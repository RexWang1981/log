import pkgutil
import importlib

def count_modules_in_package(package_name):
    package = importlib.import_module(package_name)
    module_count = 0

    for _, module_name, ispkg in pkgutil.iter_modules(package.__path__):
        module_count += 1
        print(f"Module: {module_name}, Is Package: {ispkg}")

    return module_count

package_name = 'openpyxl.cell.cell'  # 替换为你要查询的包名
module_count = count_modules_in_package(package_name)

print("Below models are in the package：", package_name)
print(f"Total number of modules in package '{package_name}': {module_count}")



