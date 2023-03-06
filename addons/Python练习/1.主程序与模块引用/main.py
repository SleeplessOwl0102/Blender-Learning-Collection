# This is a sample Python script.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from可以不用加模组名，直接导入模组中的函数
from module_test import *

# import导入模组，需要加模组名
import module_two

def print_hi(name):
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

# 不是def或class定义的代码块，都会在程序运行时执行，包含被导入的模块中的代码块也会直接执行
# __name__是python内置的变量，用来判断当前文件是主程序还是被导入的模块
print("File one __name__ is set to: {}" .format(__name__))

# python使用__name__ == '__main__'来判断当前文件是否是主程序
if __name__ == '__main__':
    print('main是主程序')
    print_hi('PyCharm')
    module_test_function()
    module_two.module_two_function()
else:
    print('main是被导入的模块')

