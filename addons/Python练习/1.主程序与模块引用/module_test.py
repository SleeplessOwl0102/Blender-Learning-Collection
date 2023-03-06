# 不是def或class定义的代码块，都会在程序运行时执行
print("File module_test.py __name__ is set to: {}" .format(__name__))

def module_test_function():
    print("这是module test function")

if __name__ == '__main__':
    print('module_test 是主程序')
else:
    print('module_test 是被导入的模块')